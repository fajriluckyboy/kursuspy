#!/usr/bin/env python3
"""Membuktikan except induk menangkap anak, tetapi tidak sebaliknya."""

import os


def buat_folder_ganda():
    """Membuat folder uji dua kali, sehingga kedua kali memicu FileExistsError."""
    os.makedirs("folder_uji", exist_ok=True)
    os.mkdir("folder_uji")


def main():
    """Alur utama program."""
    try:
        buat_folder_ganda()
    except OSError as e:
        print("Induk OSError menangkap:", type(e).__name__)

    try:
        buat_folder_ganda()
    except FileExistsError as e:
        print("Anak FileExistsError menangkap:", type(e).__name__)

    try:
        buat_folder_ganda()
    except ValueError:
        print("Tidak tercapai: ValueError bukan induk FileExistsError")

    print("Tidak tercapai juga, program sudah berhenti")


if __name__ == "__main__":
    main()
