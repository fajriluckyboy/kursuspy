#!/usr/bin/env python3
"""Latihan menulis data ke file dengan write()."""


def main():
    """Alur utama program."""
    berkas = open("data_write.txt", "w", encoding="utf-8")
    jumlah1 = berkas.write("Baris pertama\n")
    jumlah2 = berkas.write("Baris kedua\n")
    berkas.write("Tanpa baris baru, ")
    berkas.write("lanjut di baris yang sama\n")
    nama = "Fajri"
    umur = 20
    berkas.write(f"Nama: {nama}, umur: {umur}\n")
    berkas.close()
    print("Karakter write pertama:", jumlah1)
    print("Karakter write kedua  :", jumlah2)


if __name__ == "__main__":
    main()
