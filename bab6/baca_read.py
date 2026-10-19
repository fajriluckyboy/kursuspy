#!/usr/bin/env python3
"""Latihan membaca isi file dengan read()."""


def main():
    """Alur utama program."""
    berkas = open("belanja.txt", "r", encoding="utf-8")
    seluruhnya = berkas.read()
    berkas.close()
    print("Tipe hasil:", type(seluruhnya))
    print("Jumlah karakter:", len(seluruhnya))
    print("Representasi:", repr(seluruhnya))
    print("Ditampilkan:")
    print(seluruhnya)

    berkas = open("belanja.txt", "r", encoding="utf-8")
    potongan = berkas.read(5)
    sisa = berkas.read(3)
    berkas.close()
    print("Potongan 5 karakter:", repr(potongan))
    print("Berikutnya 3 karakter:", repr(sisa))

    berkas = open("belanja.txt", "r", encoding="utf-8")
    berkas.read()
    kosong = berkas.read()
    berkas.close()
    print("Baca kedua (EOF):", repr(kosong))


if __name__ == "__main__":
    main()
