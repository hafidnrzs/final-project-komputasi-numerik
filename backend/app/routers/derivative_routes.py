from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import numpy as np
from services.utils import hitung_error_persen
from services.derivative_module import (
    selisih_maju,
    selisih_mundur,
    selisih_tengahan,
    turunan_analitik,
)


# Validasi input untuk metode turunan
class DerivativeInput(BaseModel):
    fungsi: str = Field(
        ...,
        example="x**2 - np.exp(x)",
        description="Fungsi matematika sebagai string. Gunakan 'np.' untuk fungsi NumPy (misal np.sin, np.exp). Variabel yang diizinkan adalah 'x'.",
    )
    x: float = Field(
        ..., example=1.0, description="Nilai x dimana turunan akan dihitung."
    )
    h: float = Field(
        ...,
        example=0.1,
        gt=0,
        description="Ukuran langkah (step size). Harus lebih besar dari 0.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "fungsi": "x**2",
                "x": 1.0,
                "h": 0.1,
            }
        }


# --- Endpoints ---
router = APIRouter()


@router.post("/metode/selisih-maju/", tags=["Metode Numerik"])
async def solve_selisih_maju(data: DerivativeInput):
    """
    Menghitung turunan fungsi dengan Metode Selisih Maju pada titik x dengan ukuran langkah h.
    """
    try:
        hasil_numerik = selisih_maju(data.fungsi, data.x, data.h, np_alias=np)
        try:
            hasil_analitik = turunan_analitik(data.fungsi, data.x)
            error = hitung_error_persen(hasil_numerik, hasil_analitik)

            return {
                "metode": "Selisih Maju",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": f"{error * 100}%",
            }
        except ValueError as e:
            return {
                "metode": "Selisih Maju",
                "hasil_numerik": hasil_numerik,
                "message": f"Turunan analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_selisih_maju: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )


@router.post("/metode/selisih-tengahan/", tags=["Metode Numerik"])
async def solve_selisih_tengahan(data: DerivativeInput):
    """
    Menghitung turunan fungsi dengan Metode Selisih Tengahan pada titik x dengan ukuran langkah h.
    """
    try:
        hasil_numerik = selisih_tengahan(data.fungsi, data.x, data.h, np_alias=np)
        try:
            hasil_analitik = turunan_analitik(data.fungsi, data.x)
            error = hitung_error_persen(hasil_numerik, hasil_analitik)

            return {
                "metode": "Selisih Tengahan",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": f"{error * 100}%",
            }
        except ValueError as e:
            return {
                "metode": "Selisih Tengahan",
                "hasil_numerik": hasil_numerik,
                "message": f"Turunan analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_selisih_tengahan: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )


@router.post("/metode/selisih-mundur/", tags=["Metode Numerik"])
async def solve_selisih_mundur(data: DerivativeInput):
    """
    Menghitung turunan fungsi dengan Metode Selisih Mundur pada titik x dengan ukuran langkah h.
    """
    try:
        hasil_numerik = selisih_mundur(data.fungsi, data.x, data.h, np_alias=np)
        try:
            hasil_analitik = turunan_analitik(data.fungsi, data.x)
            error = hitung_error_persen(hasil_numerik, hasil_analitik)
            return {
                "metode": "Selisih Mundur",
                "hasil_numerik": hasil_numerik,
                "hasil_analitik": hasil_analitik,
                "error": f"{error * 100}%",
            }
        except ValueError as e:
            return {
                "metode": "Selisih Mundur",
                "hasil_numerik": hasil_numerik,
                "message": f"Turunan analitik tidak dapat dihitung: {str(e)}",
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error tidak terduga di solve_selisih_mundur: {e}")
        raise HTTPException(
            status_code=500, detail=f"Terjadi kesalahan internal server: {str(e)}"
        )
