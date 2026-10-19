#!/usr/bin/env python3
"""Latihan menulis dan membaca file memakai with."""


def main():
    """Alur utama program."""
    with open("pesan.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Halo dari with\n")
        berkas.write("Baris kedua\n")
        print("Di dalam blok, tertutup?", berkas.closed)

    print("Setelah blok, tertutup?", berkas.closed)

    with open("pesan.txt", "r", encoding="utf-8") as berkas:
        for baris in berkas:
            print(repr(baris))


if __name__ == "__main__":
    main()
