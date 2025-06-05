# Komputasi Numerik Web Application

Aplikasi web untuk perhitungan numerik turunan dan integrasi menggunakan berbagai metode numerik. Proyek ini terdiri dari frontend React dan backend FastAPI untuk menyediakan antarmuka yang mudah digunakan dan perhitungan yang akurat.

## Fitur Utama

### Turunan Numerik

- Metode Selisih Maju
- Metode Selisih Mundur
- Metode Selisih Tengah

### Integrasi Numerik

- Metode Riemann
- Metode Trapezoida
- Metode Simpson

## Struktur Proyek

```
final-project-komputasi-numerik/
├── frontend/         # React frontend application
└── backend/          # FastAPI backend application
```

## Instalasi

### Backend

1. Masuk ke direktori backend

```bash
cd backend
```

2. (Disarankan) Buat dan aktifkan virtual environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Jalankan server

```bash
cd app
uvicorn main:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`

### Frontend

1. Masuk ke direktori frontend

```bash
cd frontend
```

2. Install dependencies

```bash
npm install
```

3. Jalankan aplikasi dalam mode development

```bash
npm run dev
```

Aplikasi akan berjalan di `http://localhost:5173`

## Penggunaan

1. Buka aplikasi di browser (http://localhost:5173)
2. Pilih metode perhitungan (Turunan atau Integrasi)
3. Masukkan fungsi matematika menggunakan format LaTeX
4. Isi parameter yang diperlukan sesuai metode yang dipilih
5. Klik tombol untuk mendapatkan hasil perhitungan

## Format Input

- Fungsi matematika harus dimasukkan dalam format LaTeX
- Contoh input yang valid:
  - `x^2 + 2x + 1`
  - `\frac{1}{4}(x^2 + 2x + 1)`

## Dokumentasi API

Dokumentasi API lengkap dapat diakses melalui Swagger UI di:

```
http://127.0.0.1:8000/docs
```

## Persyaratan Sistem

- Python 3.8 - 3.11 (untuk backend)
- Node.js (untuk frontend)
- Browser modern dengan dukungan JavaScript
