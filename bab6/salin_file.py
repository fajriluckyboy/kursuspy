#!/usr/bin/env python3
"""Latihan menyalin file dengan shutil.copy()."""

import os
import shutil


def main():
    """Alur utama program."""
    with open("asli.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Isi file asli\n")

    print("Salinan ada sebelum copy?", os.path.exists("salinan.txt"))
    hasil = shutil.copy("asli.txt", "salinan.txt")
    print("Nilai balik copy():", hasil)
    print("Salinan ada sesudah copy?", os.path.exists("salinan.txt"))

    with open("salinan.txt", "r", encoding="utf-8") as berkas:
        print("Isi salinan:", repr(berkas.read()))


if __name__ == "__main__":
    main()
