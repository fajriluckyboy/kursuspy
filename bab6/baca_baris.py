#!/usr/bin/env python3
"""Latihan membaca file satu baris dengan readline()."""


def main():
    """Alur utama program."""
    berkas = open("belanja.txt", "r", encoding="utf-8")
    pertama = berkas.readline()
    kedua = berkas.readline()
    print("Baris 1:", repr(pertama))
    print("Baris 2:", repr(kedua))
    berkas.close()

    berkas = open("belanja.txt", "r", encoding="utf-8")
    nomor = 1
    baris = berkas.readline()
    while baris:
        print(nomor, repr(baris))
        nomor += 1
        baris = berkas.readline()
    berkas.close()
    print("Selesai, baris terakhir:", repr(baris))


if __name__ == "__main__":
    main()
