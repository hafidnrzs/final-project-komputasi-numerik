# Komputasi Numerik Web Application

Aplikasi web untuk perhitungan numerik turunan dan integrasi menggunakan berbagai metode numerik.

## Fitur

### Turunan Numerik

- Metode Selisih Maju
- Metode Selisih Mundur
- Metode Selisih Tengah

### Integrasi Numerik

- Metode Riemann
- Metode Trapezoida
- Metode Simpson

## Instalasi

1. Clone repository

```bash
git clone https://github.com/hafidnrzs/final-project-komputasi-numerik.git
cd final-project-komputasi-numerik/frontend
```

2. Install dependencies

```bash
npm install
```

3. Jalankan aplikasi dalam mode development

```bash
npm run dev
```

4. Build untuk production

```bash
npm run build
```

## Penggunaan

1. Buka aplikasi di browser (default: http://localhost:5173)
2. Pilih metode perhitungan (Turunan atau Integrasi)
3. Masukkan fungsi matematika menggunakan format LaTeX
4. Isi parameter yang diperlukan sesuai metode yang dipilih
5. Klik tombol untuk mendapatkan hasil perhitungan

## Format Input

- Fungsi matematika harus dimasukkan dalam format LaTeX
- Contoh input yang valid:
  - `x^2 + 2x + 1`
  - `\frac{1}{4}(x^2 + 2x + 1)`
