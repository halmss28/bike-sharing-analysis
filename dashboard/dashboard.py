import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

st.write("✅ App berhasil dimulai.")

st.title("📊 Dashboard Analisis Peminjaman Sepeda")


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/day.csv", parse_dates=["dteday"])
    season_map = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
    df['Musim'] = df['season'].map(season_map)
    return df

data = load_data()

# Sidebar Filter
st.sidebar.header("Filter")

# Filter musim
musim = st.sidebar.multiselect(
    "Pilih Musim",
    options=data["Musim"].unique(),
    default=data["Musim"].unique()
)

# Filter tanggal
min_date = data["dteday"].min()
max_date = data["dteday"].max()
start_date = st.sidebar.date_input("Tanggal Awal", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("Tanggal Akhir", min_value=min_date, max_value=max_date, value=max_date)

# Validasi tanggal
if start_date > end_date:
    st.sidebar.error("Tanggal awal tidak boleh melebihi tanggal akhir!")
    st.stop()

# Filter tahun untuk tren bulanan
tahun_tersedia = sorted(data["dteday"].dt.year.unique())
default_index = tahun_tersedia.index(2012) if 2012 in tahun_tersedia else 0
tahun = st.sidebar.selectbox("Pilih Tahun untuk Tren Bulanan", options=tahun_tersedia, index=default_index)

# Filter data
filtered_data = data[
    (data["Musim"].isin(musim)) &
    (data["dteday"] >= pd.to_datetime(start_date)) &
    (data["dteday"] <= pd.to_datetime(end_date))
]

if filtered_data.empty:
    st.warning("⚠️ Data kosong. Silakan ubah filter untuk melihat visualisasi.")
    st.stop()

# Filter khusus tren bulanan (agregasi per bulan)
filtered_data_tahun = filtered_data[filtered_data["dteday"].dt.year == tahun]

# Agregasi data per bulan
monthly_data = filtered_data_tahun.resample('M', on='dteday').agg({'cnt': 'sum'}).reset_index()

# Grafik Tren Bulanan
st.subheader(f"📈 Tren Jumlah Peminjaman Sepeda per Bulan (Tahun {tahun})")
fig1, ax1 = plt.subplots(figsize=(14, 5))
sns.lineplot(data=monthly_data, x="dteday", y="cnt", ax=ax1, color='dodgerblue', 
             marker='o', linestyle='-', linewidth=2, markersize=7)
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Jumlah Peminjaman")
ax1.set_title(f"Tren Peminjaman Sepeda per Bulan ({tahun})")
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
st.pyplot(fig1)

# Grafik Rata-Rata Peminjaman per Musim
st.subheader("🌤️ Rata-Rata Peminjaman per Musim")
fig2, ax2 = plt.subplots(figsize=(6, 4))
avg_per_season = filtered_data.groupby("Musim")["cnt"].mean().reindex(['Semi', 'Panas', 'Gugur', 'Dingin'])
sns.barplot(x=avg_per_season.index, y=avg_per_season.values, ax=ax2, palette="viridis")
ax2.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig2)

# Grafik Weekday vs Weekend
st.subheader("📅 Rata-Rata Peminjaman: Weekday vs Weekend")
filtered_data = filtered_data.copy()
filtered_data["day_type"] = filtered_data["weekday"].apply(lambda x: "Weekend" if x >= 5 else "Weekday")
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.barplot(data=filtered_data, x="day_type", y="cnt", ax=ax3, palette="coolwarm")
ax3.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig3)

