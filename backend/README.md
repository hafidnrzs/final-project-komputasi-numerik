## Instalasi

Disarankan menggunakan Python >=3.8

Install library dan dependency
```
pip install -r requirements.txt
```

Untuk menjalankan aplikasi (gunakan perintah uvicorn di terminal):
```
uvicorn main:app --reload
```

Contoh permintaan ke `/metode/integrasi-riemann/` menggunakan curl:
```
curl -X POST "http://127.0.0.1:8000/metode/integrasi-riemann/" \
-H "Content-Type: application/json" \
-d '{
    "fungsi": "x**2",
    "h": 0.1,
    "batas_bawah": 0.0,
    "batas_atas": 1.0
}'
