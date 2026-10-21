#!/usr/bin/env python3
"""Membuktikan assert hilang di mode -O, sedangkan raise tetap bekerja."""


def umur_dengan_assert(umur):
    """Memeriksa umur memakai assert (cara yang salah untuk masukan)."""
    assert umur >= 0, "umur tidak boleh negatif"
    return umur


def umur_dengan_raise(umur):
    """Memeriksa umur memakai raise (cara yang benar untuk masukan)."""
    if umur < 0:
        raise ValueError("umur tidak boleh negatif")
    return umur


def coba(fungsi, nilai):
    """Memanggil fungsi dan melaporkan hasil atau jenis errornya."""
    try:
        hasil = fungsi(nilai)
    except (AssertionError, ValueError) as e:
        print(f"{fungsi.__name__}({nilai}) -> ditolak: {type(e).__name__}")
    else:
        print(f"{fungsi.__name__}({nilai}) -> diterima: {hasil}")


def main():
    """Alur utama program."""
    print("__debug__ =", __debug__)
    coba(umur_dengan_assert, -5)
    coba(umur_dengan_raise, -5)


if __name__ == "__main__":
    main()
