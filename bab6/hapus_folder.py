#!/usr/bin/env python3
"""Latihan menghapus direktori dengan os.rmdir() dan shutil.rmtree()."""

import os
import shutil


def main():
    """Alur utama program."""
    os.makedirs("sampah/dalam", exist_ok=True)
    with open("sampah/dalam/isi.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Isi folder\n")

    os.makedirs("kosong", exist_ok=True)
    print("kosong ada sebelum?", os.path.isdir("kosong"))
    hasil = os.rmdir("kosong")
    print("Nilai balik rmdir():", hasil)
    print("kosong ada sesudah?", os.path.isdir("kosong"))

    print("sampah ada sebelum?", os.path.isdir("sampah"))
    shutil.rmtree("sampah")
    print("sampah ada sesudah?", os.path.isdir("sampah"))


if __name__ == "__main__":
    main()
