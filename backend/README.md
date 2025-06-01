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

Terakhir diuji menggunakan Python 3.8

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

## Format Input Fungsi Matematika

API ini menggunakan format input LaTex untuk fungsi matematika:
   - Tulis fungsi dalam notasi LaTeX tanpa tanda dollar ($)
   - Contoh: `x^2 + \sin(x)`, `\frac{1}{x} + e^x`

## Contoh Penggunaan API

1. Menghitung Turunan dengan Metode Selisih Maju:
```bash
curl -X POST "http://127.0.0.1:8000/metode/selisih-maju/" \
-H "Content-Type: application/json" \
-d '{
    "fungsi": "x^2",
    "x": 1.0,
    "h": 0.1
}'
```

2. Menghitung Integral dengan Metode Riemann:
```bash
curl -X POST "http://127.0.0.1:8000/metode/integrasi-riemann/" \
-H "Content-Type: application/json" \
-d '{
    "fungsi": "x^2",
    "h": 0.1,
    "batas_bawah": 0.0,
    "batas_atas": 1.0
}'
```
