#!/usr/bin/env python3
"""Pembanding: tanpa penangkap di lapisan atas."""


def periksa_umur(umur):
    """Mengembalikan umur bila sah, memicu ValueError bila tidak."""
    if umur < 0:
        raise ValueError(f"umur tidak boleh negatif: {umur}")
    if umur > 150:
        raise ValueError(f"umur tidak masuk akal: {umur}")
    return umur


def main():
    """Alur utama program."""
    umur = periksa_umur(int(input("Masukkan umur: ")))
    print("Umur diterima:", umur)


if __name__ == "__main__":
    main()
