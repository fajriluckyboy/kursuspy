#!/usr/bin/env python3
"""Latihan raise ulang dan rantai error dengan raise from."""


def baca_konfigurasi(nama):
    """Membaca file konfigurasi, error dibungkus dengan pesan yang jelas."""
    try:
        with open(nama, "r", encoding="utf-8") as berkas:
            return berkas.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"konfigurasi {nama!r} tidak tersedia") from e


def catat_lalu_teruskan():
    """Mencatat error, lalu melemparnya ulang apa adanya."""
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("Dicatat: ada pembagian nol")
        raise


def main():
    """Alur utama program."""
    try:
        catat_lalu_teruskan()
    except ZeroDivisionError as e:
        print("main menerima ulang:", type(e).__name__)

    try:
        baca_konfigurasi("tidak_ada.cfg")
    except RuntimeError as e:
        print("Error baru   :", type(e).__name__, "-", e)
        print("Penyebabnya  :", type(e.__cause__).__name__)

    baca_konfigurasi("tidak_ada.cfg")


if __name__ == "__main__":
    main()
