import numpy as np


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
    hasil_error = abs((hasil_numerik - hasil_analitik) / hasil_analitik)
    return round(hasil_error, 4)


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
