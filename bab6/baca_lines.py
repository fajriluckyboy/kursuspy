#!/usr/bin/env python3
"""Latihan membaca semua baris file dengan readlines()."""


def main():
    """Alur utama program."""
    berkas = open("belanja.txt", "r", encoding="utf-8")
    semua = berkas.readlines()
    kosong = berkas.readlines()
    berkas.close()
    print("Tipe hasil:", type(semua))
    print("Isi list:", semua)
    print("Jumlah baris:", len(semua))
    print("Baris ke-2:", repr(semua[1]))
    print("Baca kedua (EOF):", kosong)

    for nomor, baris in enumerate(semua, 1):
        print(nomor, repr(baris))


if __name__ == "__main__":
    main()
