# API Metode Numerik

Proyek ini merupakan implementasi berbagai metode numerik untuk menyelesaikan perhitungan turunan dan integral menggunakan FastAPI. API ini menyediakan endpoint untuk:

**Turunan:**

- Metode Selisih Maju
- Metode Selisih Tengah
- Metode Selisih Mundur

**Integral:**

- Metode Riemann
- Metode Trapezoida
- Metode Simpson

Terakhir diuji menggunakan Python 3.8 - 3.11

## Instalasi

1. Clone repository ini
```bash
git clone https://github.com/hafidnrzs/final-project-komputasi-numerik.git
cd final-project-komputasi-numerik/backend
```

2. (Disarankan) Buat dan aktifkan virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Install library dan dependency yang dibutuhkan
```bash
pip install -r requirements.txt
```

## Menjalankan Aplikasi

1. Masuk ke direktori app
```bash
cd app
```

2. Jalankan server dengan uvicorn
```bash
uvicorn main:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`

Setelah server berjalan, dokumentasi API lengkap dapat dibuka melalui Swagger UI di:
```
http://127.0.0.1:8000/docs
```

Dokumentasi ini menyediakan deskripsi lengkap semua endpoint yang tersedia, request body yang diperlukan, dan dapat mencoba API secara langsung melalui antarmuka web yang interaktif.

## Format Input Fungsi Matematika

API ini menggunakan format input LaTex untuk fungsi matematika:
   - Tulis fungsi dalam notasi LaTeX tanpa tanda dollar ($)
   - Contoh: `x^2`, `\frac{1}{x} + e^x`
