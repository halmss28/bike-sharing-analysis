# 📊 Bike Sharing Data Analysis Dashboard

## 📝 Deskripsi
Dashboard ini menyajikan analisis interaktif terkait peminjaman sepeda harian berdasarkan data historis dari Capital Bikeshare (Washington D.C).  
Pengguna dapat memfilter data berdasarkan **musim**, **tanggal**, dan **tahun**, serta melihat berbagai visualisasi tren peminjaman.

---

## 📁 Struktur Folder

```
bike-sharing-analysis/
├── dashboard/
│   ├── dashboard.py         # File utama Streamlit
│   └── day.csv              # Dataset harian
├── data/                    # (Opsional) Folder tambahan untuk data
├── notebook.ipynb           # Analisis eksploratif (opsional)
├── requirements.txt         # Dependensi Python
├── .streamlit/config.toml   # Konfigurasi versi Python Streamlit
├── README.md
└── url.txt                  # Link Streamlit Cloud (jika ada)
```

---

## ▶️ Cara Menjalankan Dashboard Secara Lokal

1. **Clone repository**:
   ```bash
   git clone https://github.com/halmss28/bike-sharing-analysis.git
   cd bike-sharing-analysis
   ```

2. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Streamlit app**:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

---

## 🌐 Link Aplikasi Live (jika tersedia)

Lihat di file [`url.txt`](url.txt) atau buka langsung:
```
https://bike-sharing-analysis-halmss28.streamlit.app/
```

---

## 📌 Catatan

- File `day.csv` harus berada di dalam folder `dashboard/` agar bisa diakses saat deploy.
- Pastikan menggunakan Python 3.10 (sudah diatur lewat `.streamlit/config.toml`).
