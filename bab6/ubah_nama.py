#!/usr/bin/env python3
"""Latihan mengubah nama file dengan os.rename()."""

import os


def main():
    """Alur utama program."""
    with open("nama_lama.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Isi tidak berubah\n")

    print("nama_lama ada sebelum?", os.path.exists("nama_lama.txt"))
    print("nama_baru ada sebelum?", os.path.exists("nama_baru.txt"))

    hasil = os.rename("nama_lama.txt", "nama_baru.txt")
    print("Nilai balik rename():", hasil)

    print("nama_lama ada sesudah?", os.path.exists("nama_lama.txt"))
    print("nama_baru ada sesudah?", os.path.exists("nama_baru.txt"))

    with open("nama_baru.txt", "r", encoding="utf-8") as berkas:
        print("Isi nama_baru:", repr(berkas.read()))


if __name__ == "__main__":
    main()
