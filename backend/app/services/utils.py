import numpy as np
from sympy.parsing.latex import parse_latex
import re


def parse_latex_to_python(latex_str: str) -> str:
    """
    Mengkonversi ekspresi LaTeX ke ekspresi Python yang valid.

    Args:
        latex_str (str): Ekspresi matematika dalam format LaTeX.

    Returns:
        str: Ekspresi matematika dalam format Python.

    Raises:
        ValueError: Jika ekspresi LaTeX tidak valid atau tidak dapat dikonversi.
    """
    try:
        latex_str = latex_str.strip("$")
        sympy_expr = parse_latex(latex_str)
        python_str = str(sympy_expr)
        replacements = {
            "sin": "np.sin",
            "cos": "np.cos",
            "tan": "np.tan",
            "exp": "np.exp",
            "log": "np.log",
            "sqrt": "np.sqrt",
            "pi": "np.pi",
            "e": "np.e",
        }

        for old, new in replacements.items():
            python_str = re.sub(r"\b" + old + r"\b", new, python_str)
        return python_str
    except Exception as e:
        raise ValueError(f"Error saat mengurai ekspresi LaTeX: {str(e)}")


def eval_func(fungsi_str: str, x: float, np_alias=np):
    """
    Mengevaluasi string fungsi matematika.

    Args:
        fungsi_str (str): Fungsi sebagai string, misal "x**3 + x**2".
        x (float): Nilai variabel x untuk evaluasi.
        np_alias: Alias untuk library numpy yang bisa digunakan dalam fungsi_str.

    Returns:
        float: Hasil evaluasi fungsi.

    Raises:
        ValueError: Jika terjadi error saat mengevaluasi fungsi
    """
    try:
        allowed_names = {
            "x": x,
            "np": np_alias,
            "sqrt": np_alias.sqrt,
            "pi": np_alias.pi,
            "e": np_alias.e,
        }
        return eval(fungsi_str, {"__builtins__": {}}, allowed_names)
    # except NameError as e:
    #     raise ValueError(
    #         f"Error: Nama tidak dikenal dalam fungsi: {e}. Pastikan menggunakan hanya variabel 'x'."
    #     )
    except SyntaxError as e:
        raise ValueError(f"Error: Kesalahan sintaks dalam fungsi: {e}")
    except Exception as e:
        raise ValueError(
            f"Error saat mengevaluasi fungsi '{fungsi_str}' pada x={x}: {e}"
        )


def hitung_error(numerik: float, analitik: float):
    """
    Menghitung nilai error dalam perhitunga metode numerik

    Args:
        numerik (float): Hasil dari perhitungan metode numerik
        analitik (float): Hasil dari perhitungan metode analitik

    Returns:
        float: Nilai error
    """
    hasil_error = abs(numerik - analitik)
    return round(hasil_error, 3)


def hitung_error_persen(hasil_numerik, hasil_analitik):
    """
    Menghitung nilai error dalam perhitunga metode numerik dalam persen

    Args:
        numerik (float): Hasil dari perhitungan metode numerik
        analitik (float): Hasil dari perhitungan metode analitik

    Returns:
        float: Nilai error dalam persen
    """
    if hasil_analitik == 0:
        hasil_error = abs(hasil_numerik)
    else:
        hasil_error = abs((hasil_numerik - hasil_analitik) / hasil_analitik)
    error_persen = hasil_error * 100

    return round(error_persen, 3)


def hitung_h(batas_bawah: float, batas_atas: float, N: int):
    """
    Menghitung ukuran langkah (step size) h jika diketahui nilai N

    Args:
        batas_bawah (float): Batas bawah iterasi
        batas_atas (float): Batas atas iterasi
        N (int): Jumlah segmen yang diinginkan

    Returns:
        float: Ukuran langkah (step size) h
    """
    return (batas_atas - batas_bawah) / N
