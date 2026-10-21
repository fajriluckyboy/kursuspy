#!/usr/bin/env python3
"""Latihan dasar raise: memicu eksepsi dari kode sendiri."""


def periksa_umur(umur):
    """Mengembalikan umur bila sah, memicu error bila tidak."""
    if not isinstance(umur, int):
        raise TypeError(f"umur harus int, bukan {type(umur).__name__}")
    if umur < 0:
        raise ValueError(f"umur tidak boleh negatif: {umur}")
    return umur


def coba(umur):
    """Memanggil periksa_umur() dan melaporkan hasilnya."""
    try:
        hasil = periksa_umur(umur)
    except (TypeError, ValueError) as e:
        print(f"Ditolak  : {type(e).__name__}: {e}")
    else:
        print("Diterima :", hasil)


def main():
    """Alur utama program."""
    coba(20)
    coba(-5)
    coba("dua puluh")
    print(periksa_umur(-1))
    print("Tidak tercapai: error terakhir tidak ditangani")


if __name__ == "__main__":
    main()
