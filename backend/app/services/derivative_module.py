import numpy as np
from sympy import diff, Symbol, latex
from services.utils import eval_func

x = Symbol("x")


def turunan_analitik(fungsi_str: str, nilai_x: float):
    """
    Menghitung turunan secara analitik menggunakan sympy.

    Args:
        fungsi_str (str): Fungsi sebagai string
        nilai_x (float): Nilai x dimana turunan akan dihitung

    Returns:
        float: Hasil turunan analitik yang sudah dievaluasi
        str: Turunan fungsi dalam format LaTeX

    Raises:
        ValueError: Jika fungsi tidak bisa diturunkan secara analitik
    """
    try:
        turunan = diff(fungsi_str, x)
        turunan_latex = latex(turunan)
        hasil_analitik = turunan.subs(x, nilai_x)

        # Konversi ke float dan bulatkan
        if hasattr(hasil_analitik, "evalf"):
            return round(float(hasil_analitik.evalf()), 3), turunan_latex
        return (round(float(hasil_analitik), 3)), turunan_latex
    except Exception as e:
        raise ValueError(f"Gagal menghitung turunan analitik: {str(e)}")


def selisih_maju(fungsi_str: str, x: float, h: float, np_alias=np):
    """
    Menghitung turunan fungsi dengan Metode Selisih Maju

    Args:
        fungsi_str (str): Fungsi sebagai string
        x (float): Nilai x dari fungsi
        h (float): Ukuran langkah (step size)

    Returns:
        float: Nilai numerik
    """
    result = (
        eval_func(fungsi_str, x + h, np_alias) - eval_func(fungsi_str, x, np_alias)
    ) / h
    return round(result, 3)


def selisih_tengahan(fungsi_str: str, x: float, h: float, np_alias=np):
    """
    Menghitung turunan fungsi dengan Metode Selisih Tengahan

    Args:
        fungsi_str (str): Fungsi sebagai string
        x (float): Nilai x dari fungsi
        h (float): Ukuran langkah (step size)

    Returns:
        float: Nilai numerik
    """
    result = (
        eval_func(fungsi_str, x + h, np_alias) - eval_func(fungsi_str, x - h, np_alias)
    ) / (2 * h)
    return round(result, 3)


def selisih_mundur(fungsi_str: str, x: float, h: float, np_alias=np):
    """
    Menghitung turunan fungsi dengan Metode Selisih Mundur

    Args:
        fungsi_str (str): Fungsi sebagai string
        x (float): Nilai x dari fungsi
        h (float): Ukuran langkah (step size)

    Returns:
        float: Nilai numerik
    """
    result = (
        eval_func(fungsi_str, x, np_alias) - eval_func(fungsi_str, x - h, np_alias)
    ) / h
    return round(result, 3)
