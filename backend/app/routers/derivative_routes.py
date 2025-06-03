from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from typing import Optional
import numpy as np

from services.utils import hitung_error_persen, parse_latex_to_python
from services.derivative_module import (
    selisih_maju,
    selisih_mundur,
    selisih_tengahan,
    turunan_analitik,
)

# --- Router Setup ---
router = APIRouter(prefix="/turunan", tags=["Metode Numerik Turunan"])


# --- Response Model ---
class DerivativeCalcResponse(BaseModel):
    metode: str
    input_fungsi: str
    input_x: float
    input_h: float
    hasil_numerik: float
    hasil_analitik: Optional[float] = None
    error_relatif: Optional[str] = None


# --- Endpoints ---
@router.post("/", response_model=DerivativeCalcResponse)
async def solve_derivative_form(
    metode: str = Form(
        description="Metode turunan numerik yang akan digunakan: _selisih-maju_, _selisih_tengahan_, _selisih-mundur_"
    ),
    fungsi_latex: str = Form(
        description="Fungsi matematika dalam format LaTex. Contoh: _x^2_ atau _\\frac{1}{2}x_"
    ),
    x: float = Form(description="Nilai x di mana turunan akan dihitung."),
    h_step: float = Form(
        alias="h",
        description="Ukuran langkah (step size). Harus lebih besar dari 0.",
        gt=0,  # h > 0
    ),
):
    """
    Menghitung turunan dari suatu fungsi menggunakan metode numerik yang dipilih.
    """

    # Parsing fungsi LaTeX ke ekspresi Python
    try:
        fungsi_python = parse_latex_to_python(fungsi_latex)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Gagal mem-parsing fungsi LaTeX: {str(e)}"
        )
    hasil_numerik = 0.0

    # Pemilihan metode dan perhitungan
    try:
        if metode == "selisih-maju":
            hasil_numerik = selisih_maju(fungsi_python, x, h_step, np_alias=np)
        elif metode == "selisih-tengahan":
            hasil_numerik = selisih_tengahan(fungsi_python, x, h_step, np_alias=np)
        elif metode == "selisih-mundur":
            hasil_numerik = selisih_mundur(fungsi_python, x, h_step, np_alias=np)

        # Hitung metode analitik dan cari error
        try:
            hasil_analitik = turunan_analitik(fungsi_python, x)
            error_relatif = hitung_error_persen(hasil_numerik, hasil_analitik) * 100
        except ValueError as ve_analitik:
            raise HTTPException(
                status_code=400,
                detail=f"Turunan analitik tidak dapat dihitung: {str(ve_analitik)}",
            )

        return DerivativeCalcResponse(
            metode=metode,
            input_fungsi=fungsi_latex,
            input_x=x,
            input_h=h_step,
            hasil_numerik=hasil_numerik,
            hasil_analitik=hasil_analitik,
            error_relatif=str(error_relatif) + "%",
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except HTTPException:
        raise
    except Exception:
        # print(f"Error tidak terduga di solve_derivative_form: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan di server.")
