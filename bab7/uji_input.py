#!/usr/bin/env python3
"""Menguji raise dengan input: lapisan dalam melapor, lapisan atas menangani."""


def periksa_umur(umur):
    """Mengembalikan umur bila sah, memicu ValueError bila tidak."""
    if umur < 0:
        raise ValueError(f"umur tidak boleh negatif: {umur}")
    if umur > 150:
        raise ValueError(f"umur tidak masuk akal: {umur}")
    return umur


def minta_umur():
    """Meminta umur sampai pengguna memberi nilai yang sah."""
    while True:
        teks = input("Masukkan umur: ")
        try:
            umur = periksa_umur(int(teks))
        except ValueError as e:
            print(f"Umur tidak valid ({e}). Coba lagi.")
        else:
            return umur


def main():
    """Alur utama program."""
    umur = minta_umur()
    print("Umur diterima:", umur)


if __name__ == "__main__":
    main()
