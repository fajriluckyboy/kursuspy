#!/usr/bin/env python3
"""Latihan membuka file dan memeriksa objek file."""


def main():
    """Alur utama program."""
    berkas = open("catatan.txt", "w", encoding="utf-8")
    print("Tipe objek:", type(berkas))
    print("Nama file :", berkas.name)
    print("Mode      :", berkas.mode)
    print("Encoding  :", berkas.encoding)
    print("Tertutup? :", berkas.closed)
    berkas.close()
    print("Tertutup? :", berkas.closed)


if __name__ == "__main__":
    main()
