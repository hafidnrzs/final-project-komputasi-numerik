from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator
from typing import Optional, Any
import numpy as np

from numerical_methods import (
    hitung_h,
    cara_analitik,
    hitung_error,
    riemann_integral,
    trapezoida_integral,
    simpson_integral,
)

app = FastAPI(
    title="API Metode Numerik",
    description="API untuk menyelesaikan berbagai metode numerik.",
    version="0.1.0",
)


# Validasi input
class NumericalInput(BaseModel):
    fungsi: str = Field(
        ...,
        example="x**2 - np.exp(x)",
        description="Fungsi matematika sebagai string. Gunakan 'np.' untuk fungsi NumPy (misal np.sin, np.exp). Variabel yang diizinkan adalah 'x'.",
    )
    batas_bawah: float = Field(
        ..., example=0.0, description="Batas bawah interval atau iterasi."
    )
    batas_atas: float = Field(
        ..., example=1.0, description="Batas atas interval atau iterasi."
    )
    h: Optional[float] = Field(
        default=None,
        example=0.1,
        description="Ukuran langkah (step size). Opsional jika N disediakan.",
    )
    N: Optional[int] = Field(
        default=None,
        example=10,
        ge=1,
        description="Jumlah sub-interval. Opsional jika h disediakan. Harus bilangan bulat positif.",
    )

    @model_validator(mode="after")
    def check_h_or_n_exclusive(cls, values: Any) -> Any:
        h_val = values.h
        n_val = values.N
        batas_bawah_val = values.batas_bawah
        batas_atas_val = values.batas_atas

        if h_val is None and n_val is None:
            raise ValueError("Salah satu dari 'h' atau 'N' wajib disediakan.")

        if n_val is not None:
            try:
                calculated_h = hitung_h(batas_bawah_val, batas_atas_val, n_val)
                if calculated_h == 0:
                    raise ValueError(
                        "Kombinasi batas_bawah, batas_atas, dan N menghasilkan h = 0, yang tidak valid."
                    )
                values.h = calculated_h
            except ValueError as e:
                raise ValueError(str(e))

        if h_val is not None and h_val == 0:
            raise ValueError("Ukuran langkah (h) tidak boleh nol.")

        return values

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "summary": "Contoh dengan h",
                    "value": {
                        "fungsi": "x**3 - 2*x + 5",
                        "h": 0.05,
                        "batas_bawah": -2.0,
                        "batas_atas": 2.0,
                    },
                },
                {
                    "summary": "Contoh dengan N",
                    "value": {
                        "fungsi": "np.sin(x)",
                        "N": 20,
                        "batas_bawah": 0.0,
                        "batas_atas": np.pi,
                    },
                },
            ]
        }


# --- Endpoints ---
@app.post("/metode/integrasi-riemann/", tags=["Metode Numerik"])
async def solve_riemann_integral(data: NumericalInput):
    """
    Menjalankan metode numerik Integral Riemann yang mengevaluasi fungsi
    pada interval [batas_bawah, batas_atas] dengan langkah h.
    """
    if data.h <= 0:
        raise HTTPException(
            status_code=400, detail="Ukuran langkah (h) tidak boleh nol atau negatif."
        )

    if data.h > 0 and data.batas_bawah > data.batas_atas:
        raise HTTPException(
            status_code=400,
            detail="batas_bawah harus lebih kecil dari batas_atas.",
        )

    try:
        hasil_numerik = riemann_integral(
            data.fungsi,
            data.h,
            data.batas_bawah,
            data.batas_atas,
            np_alias=np,
        )
        try:
            hasil_analitik = cara_analitik(
                data.fungsi, data.batas_bawah, data.batas_atas
            )
            error = hitung_error(hasil_numerik, hasil_analitik)

            return {
                "metode": "Integrasi Riemann",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": error,
            }
        except ValueError as e:
            return {
                "metode": "Integrasi Riemann",
                "hasil_numerik": hasil_numerik,
                "pesan": f"Integral analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_riemann_integral: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )


@app.post("/metode/integrasi-trapezoida/", tags=["Metode Numerik"])
async def solve_trapezoida_integral(data: NumericalInput):
    """
    Menjalankan metode numerik Integral Trapezoida yang mengevaluasi fungsi
    pada interval [batas_bawah, batas_atas] dengan N tertentu.
    """
    if data.N <= 0:
        raise HTTPException(
            status_code=400, detail="Jumlah segmen (N) tidak boleh nol atau negatif."
        )

    if data.batas_bawah > data.batas_atas:
        raise HTTPException(
            status_code=400,
            detail="batas_bawah harus lebih kecil dari batas_atas.",
        )

    try:
        hasil_numerik = trapezoida_integral(
            data.fungsi,
            data.N,
            data.batas_bawah,
            data.batas_atas,
            np_alias=np,
        )
        try:
            hasil_analitik = cara_analitik(
                data.fungsi, data.batas_bawah, data.batas_atas
            )
            error = hitung_error(hasil_numerik, hasil_analitik)

            return {
                "metode": "Integrasi Trapezoida",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": error,
            }
        except ValueError as e:
            return {
                "metode": "Integrasi Riemann",
                "hasil_numerik": hasil_numerik,
                "pesan": f"Integral analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_trapezoida_integral: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )


@app.post("/metode/integrasi-simpson/", tags=["Metode Numerik"])
async def solve_simpson_integral(data: NumericalInput):
    """
    Menjalankan metode numerik Integral Simspon yang mengevaluasi fungsi
    pada interval [batas_bawah, batas_atas] dengan N tertentu.
    """
    if data.N <= 0:
        raise HTTPException(
            status_code=400, detail="Jumlah segmen (N) tidak boleh nol atau negatif."
        )

    if data.batas_bawah > data.batas_atas:
        raise HTTPException(
            status_code=400,
            detail="batas_bawah harus lebih kecil dari batas_atas.",
        )

    try:
        hasil_numerik = simpson_integral(
            data.fungsi,
            data.N,
            data.batas_bawah,
            data.batas_atas,
            np_alias=np,
        )
        try:
            hasil_analitik = cara_analitik(
                data.fungsi, data.batas_bawah, data.batas_atas
            )
            error = hitung_error(hasil_numerik, hasil_analitik)

            return {
                "metode": "Integrasi Simpson",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": error,
            }
        except ValueError as e:
            return {
                "metode": "Integrasi Riemann",
                "hasil_numerik": hasil_numerik,
                "pesan": f"Integral analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_simpson_integral: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )


# --- Endpoint Health Check ---
@app.get("/", tags=["Health Check"])
async def health_check():
    """
    Endpoint root untuk informasi API.
    """
    return {
        "message": "Selamat datang di API Metode Numerik!",
        "status": "healthy",
    }
