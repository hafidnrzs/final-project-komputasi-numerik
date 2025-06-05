import numpy as np
from sympy import integrate, Symbol, latex, parse_expr
from services.utils import hitung_h, eval_func

x = Symbol("x")


def integral_analitik(fungsi_str, batas_bawah, batas_atas):
    """
    Menghitung integral secara analitik menggunakan sympy.

    Args:
        fungsi_str (str): Fungsi sebagai string
        batas_bawah (float): Batas bawah integral
        batas_atas (float): Batas atas integral

    Returns:
        float: Hasil integral analitik yang sudah dievaluasi
        str: Integral fungsi dalam format LaTeX

    Raises:
        ValueError: Jika fungsi tidak bisa diintegrasikan secara analitik
    """
    try:
        hasil_integral = integrate(fungsi_str, (x, batas_bawah, batas_atas))

        fungsi = parse_expr(fungsi_str)
        integral_fungsi = integrate(fungsi_str, x)
        latex_integral = rf"\int_{{{batas_bawah}}}^{{{batas_atas}}} {latex(fungsi)}dx = \left[ {latex(integral_fungsi)} \right]_{{{batas_bawah}}}^{{{batas_atas}}}"

        # Evaluasi hasil ke nilai numerik
        if hasattr(hasil_integral, "evalf"):
            return round(float(hasil_integral.evalf()), 3), latex_integral
        return round(float(hasil_integral), 3)
    except Exception as e:
        raise ValueError(f"Gagal menghitung integral analitik: {str(e)}")


def riemann_integral(
    fungsi_str: str, h: float, batas_bawah: float, batas_atas: float, np_alias=np
):
    """
    Integrasi numerik dengan Metode Riemann

    Args:
        fungsi_str (str): Fungsi sebagai string
        h (float): Ukuran langkah (step size)
        batas_bawah (float): Batas bawah iterasi
        batas_atas (float): Batas atas iterasi

    Returns:
        float: Nilai numerik

    Raises:
        ValueError: Jika h adalah nol atau evaluasi fungsi gagal
    """
    if h == 0:
        raise ValueError("Ukuran langkah (h) tidak boleh nol.")

    i = batas_bawah
    iter_result = 0
    while i <= batas_atas:
        iter_result += eval_func(fungsi_str, i, np_alias)
        i += h
    result = h * iter_result

    return round(result, 3)


def trapezoida_integral(
    fungsi_str: str, N: int, batas_bawah: float, batas_atas: float, np_alias=np
):
    """
    Integrasi numerik dengan Metode Trapezoida

    Args:
        fungsi_str (str): Fungsi sebagai string
        N (int): Jumlah segmen
        batas_bawah (float): Batas bawah iterasi
        batas_atas (float): Batas atas iterasi

    Returns:
        float: Nilai numerik

    Raises:
        ValueError: Jika h adalah nol atau evaluasi fungsi gagal
    """
    h = hitung_h(batas_bawah, batas_atas, N)
    if h == 0:
        raise ValueError("Ukuran langkah (h) tidak boleh nol.")

    # x_0 = batas bawah
    x = batas_bawah
    f_0 = eval_func(fungsi_str, batas_bawah, np_alias)
    # x_n = batas atas
    f_n = eval_func(fungsi_str, batas_atas, np_alias)

    iter_result = 0
    for i in range(1, N):
        # x_1 = x_0 + h
        # x_2 = x_1 + h
        # ...
        x += h
        iter_result += eval_func(fungsi_str, x)
    result = h / 2 * (f_0 + 2 * iter_result + f_n)

    return round(result, 3)


def simpson_integral(
    fungsi_str: str, N: int, batas_bawah: float, batas_atas: float, np_alias=np
):
    """
    Integrasi numerik dengan Metode Simpson

    Args:
        fungsi_str (str): Fungsi sebagai string
        N (int): Jumlah segmen
        batas_bawah (float): Batas bawah iterasi
        batas_atas (float): Batas atas iterasi

    Returns:
        float: Nilai numerik

    Raises:
        ValueError: Jika h adalah nol atau evaluasi fungsi gagal

    """
    h = hitung_h(batas_bawah, batas_atas, N)
    if h == 0:
        raise ValueError("Ukuran langkah (h) tidak boleh nol.")

    # x_0 = batas bawah
    x = batas_bawah
    f_0 = eval_func(fungsi_str, batas_bawah, np_alias)
    # x_n = batas atas
    f_n = eval_func(fungsi_str, batas_atas, np_alias)

    iter_result = 0
    for i in range(1, N):
        # x_1 = x_0 + h
        # x_2 = x_1 + h
        # ...
        x += h
        if i % 2 == 0:  # jika i genap
            iter_result += 2 * eval_func(fungsi_str, x)
        else:  # jika i ganjil
            iter_result += 4 * eval_func(fungsi_str, x)
    result = h / 3 * (f_0 + iter_result + f_n)

    return round(result, 3)
