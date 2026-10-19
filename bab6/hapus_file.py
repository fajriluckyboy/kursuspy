#!/usr/bin/env python3
"""Latihan menghapus file dengan os.remove()."""

import os


def main():
    """Alur utama program."""
    with open("sementara.txt", "w", encoding="utf-8") as berkas:
        berkas.write("File ini akan dihapus\n")

    print("Ada sebelum hapus?", os.path.exists("sementara.txt"))
    hasil = os.remove("sementara.txt")
    print("Nilai balik remove():", hasil)
    print("Ada sesudah hapus?", os.path.exists("sementara.txt"))

    if os.path.exists("sementara.txt"):
        os.remove("sementara.txt")
        print("File dihapus")
    else:
        print("File tidak ada, tidak ada yang dihapus")


if __name__ == "__main__":
    main()
