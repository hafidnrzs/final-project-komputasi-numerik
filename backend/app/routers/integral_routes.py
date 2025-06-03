from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel
from typing import Optional
import numpy as np

from services.utils import hitung_error, hitung_h, parse_latex_to_python
from services.integral_module import (
    riemann_integral,
    trapezoida_integral,
    simpson_integral,
    integral_analitik,
)

# --- Router Setup ---
router = APIRouter(prefix="/integral", tags=["Metode Numerik Integral"])


# --- Response Model ---
class IntegralCalcResponse(BaseModel):
    metode: str
    input_fungsi: str
    input_batas_bawah: float
    input_batas_atas: float
    input_h: Optional[float] = None
    input_N: Optional[int] = None
    hasil_numerik: float
    hasil_analitik: Optional[float] = None
    error_relatif: Optional[str] = None


# --- Endpoint ---
@router.post("/", response_model=IntegralCalcResponse)
async def solve_integral_form(
    metode: str = Form(
        description="Metode integrasi numerik yang akan digunakan: _riemann_, _trapezoida_, _simpson_."
    ),
    fungsi_latex: str = Form(
        description="Fungsi matematika dalam format LaTex. Contoh: _x^2_ atau _\\frac{1}{2}x_"
    ),
    batas_bawah: float = Form(description="Batas bawah interval integrasi."),
    batas_atas: float = Form(description="Batas atas interval integrasi."),
    h_step: Optional[float] = Form(
        None,
        alias="h",
        description="Ukuran langkah (step size). Diperlukan untuk metode _riemann_. Jika N disediakan untuk metode lain, h akan dihitung",
        gt=0,  # h > 0
    ),
    N_segments: Optional[int] = Form(
        None,
        alias="N",
        description="Jumlah sub-interval/segmen. Diperlukan untuk metode _trapezoida_ dan _simpson_.",
        ge=1,  # N >= 1
    ),
):
    """
    Menghitung integral dari suatu fungsi menggunakan metode numerik yang dipilih.
    """

    # Validasi untuk input h atau N
    current_h = h_step
    current_N = N_segments

    if batas_bawah > batas_atas:
        batas_bawah, batas_atas = batas_atas, batas_bawah

    if metode in ["trapezoida", "simpson"]:
        if current_N is None:
            raise HTTPException(
                status_code=400,
                detail=f"Parameter 'N' wajib diisi untuk metode {metode}.",
            )
        try:
            current_h = hitung_h(batas_bawah, batas_atas, current_N)
            if current_h <= 0:
                raise ValueError(
                    "Ukuran langkah 'h' (step size) harus lebih besar dari 0"
                )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    elif metode == "riemann":
        if current_h is None:
            raise HTTPException(
                status_code=400,
                detail="Parameter 'h' wajib diisi untuk metode Riemann.",
            )
        if current_h <= 0:
            raise HTTPException(
                status_code=400,
                detail="Ukuran langkah 'h' (step size) harus lebih besar dari 0",
            )

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
        if metode == "riemann":
            hasil_numerik = riemann_integral(
                fungsi_python, current_h, batas_bawah, batas_atas, np_alias=np
            )
        elif metode == "trapezoida":
            hasil_numerik = trapezoida_integral(
                fungsi_python, current_N, batas_bawah, batas_atas, np_alias=np
            )
        elif metode == "simpson":
            hasil_numerik = simpson_integral(
                fungsi_python, current_N, batas_bawah, batas_atas, np_alias=np
            )

        # Hitung metode analitik dan cari error
        try:
            hasil_analitik = integral_analitik(fungsi_python, batas_bawah, batas_atas)
            error_relatif = hitung_error(hasil_numerik, hasil_analitik)
        except ValueError as ve_analitik:
            raise HTTPException(
                status_code=400,
                detail=f"Integral analitik tidak dapat dihitung: {str(ve_analitik)}",
            )

        return IntegralCalcResponse(
            metode=metode,
            input_fungsi=fungsi_latex,
            input_batas_bawah=batas_bawah,
            input_batas_atas=batas_atas,
            input_h=current_h
            if metode == "riemann"
            or (metode in ["trapezoida", "simpson"] and current_N is not None)
            else None,
            input_N=current_N if metode in ["trapezoida", "simpson"] else None,
            hasil_numerik=hasil_numerik,
            hasil_analitik=hasil_analitik,
            error_relatif=str(error_relatif),
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except HTTPException:
        raise
    except Exception:
        # print(f"Error tidak terduga di solve_integral_form: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan di server.")
