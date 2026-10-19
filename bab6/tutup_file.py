#!/usr/bin/env python3
"""Membuktikan peran close() pada penulisan file."""


def baca_ukuran(nama_file):
    """Membuka file untuk dibaca, lalu mengembalikan jumlah karakternya."""
    berkas = open(nama_file, "r", encoding="utf-8")
    isi = berkas.read()
    berkas.close()
    return len(isi)


def main():
    """Alur utama program."""
    berkas = open("tes_tutup.txt", "w", encoding="utf-8")
    berkas.write("Halo, ini baris percobaan.\n")
    print("Sebelum close(), jumlah karakter di file:", baca_ukuran("tes_tutup.txt"))
    berkas.close()
    print("Sesudah close(), jumlah karakter di file:", baca_ukuran("tes_tutup.txt"))


if __name__ == "__main__":
    main()
