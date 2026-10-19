#!/usr/bin/env python3
"""Latihan menulis banyak baris dengan writelines()."""


def main():
    """Alur utama program."""
    daftar_belanja = [
        "Beras\n",
        "Telur\n",
        "Minyak goreng\n",
    ]
    tanpa_baris_baru = ["Satu", "Dua", "Tiga"]

    berkas = open("belanja.txt", "w", encoding="utf-8")
    hasil = berkas.writelines(daftar_belanja)
    berkas.close()
    print("Nilai balik writelines():", hasil)

    berkas = open("menyatu.txt", "w", encoding="utf-8")
    berkas.writelines(tanpa_baris_baru)
    berkas.close()


if __name__ == "__main__":
    main()
