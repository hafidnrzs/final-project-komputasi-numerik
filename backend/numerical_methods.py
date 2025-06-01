import numpy as np
from sympy import integrate, Symbol

x = Symbol("x")


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
    except NameError as e:
        raise ValueError(
            f"Error: Nama tidak dikenal dalam fungsi: {e}. Pastikan menggunakan hanya variabel 'x'."
        )
    except SyntaxError as e:
        raise ValueError(f"Error: Kesalahan sintaks dalam fungsi: {e}")
    except Exception as e:
        raise ValueError(
            f"Error saat mengevaluasi fungsi '{fungsi_str}' pada x={x}: {e}"
        )


def cara_analitik(fungsi_str, batas_bawah, batas_atas):
    """
    Menghitung integral secara analitik menggunakan sympy.

    Args:
        fungsi_str (str): Fungsi sebagai string
        batas_bawah (float): Batas bawah integral
        batas_atas (float): Batas atas integral

    Returns:
        float: Hasil integral analitik yang sudah dievaluasi

    Raises:
        ValueError: Jika fungsi tidak bisa diintegrasikan secara analitik
    """
    try:
        hasil_integral = integrate(fungsi_str, (x, batas_bawah, batas_atas))

        # Evaluasi hasil ke nilai numerik
        if hasattr(hasil_integral, "evalf"):
            return round(float(hasil_integral.evalf()), 3)
        return round(float(hasil_integral), 3)
    except Exception as e:
        raise ValueError(f"Gagal menghitung integral analitik: {str(e)}")


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

    f_0 = eval_func(fungsi_str, batas_bawah, np_alias)
    f_n = eval_func(fungsi_str, batas_atas, np_alias)

    i = batas_bawah + h
    iter_result = 0
    while i < batas_atas:
        iter_result += eval_func(fungsi_str, i)
        i += h
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

    f_0 = eval_func(fungsi_str, batas_bawah, np_alias)
    f_n = eval_func(fungsi_str, batas_atas, np_alias)

    i = batas_bawah + h
    iter_result = 0
    while i < batas_atas:
        if i % 2 == 0:  # Jika genap
            iter_result += 2 * eval_func(fungsi_str, i)
        else:
            iter_result += 4 * eval_func(fungsi_str, i)
        i += h
    result = h / 3 * (f_0 + iter_result + f_n)

    return round(result, 3)
