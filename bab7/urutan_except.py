#!/usr/bin/env python3
"""Membuktikan urutan except: yang spesifik harus lebih dulu."""

import os


def buat_folder_ganda():
    """Memicu FileExistsError dengan membuat folder yang sudah ada."""
    os.makedirs("folder_uji", exist_ok=True)
    os.mkdir("folder_uji")


def main():
    """Alur utama program."""
    try:
        buat_folder_ganda()
    except FileExistsError:
        print("Cabang spesifik: folder sudah ada")
    except OSError:
        print("Cabang umum: masalah sistem lain")


if __name__ == "__main__":
    main()
