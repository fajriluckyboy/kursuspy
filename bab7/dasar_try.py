#!/usr/bin/env python3
"""Latihan dasar try-except-else."""


def ke_angka(teks):
    """Mengubah teks menjadi bilangan bulat, atau None bila gagal."""
    try:
        angka = int(teks)
    except ValueError as e:
        print("Gagal mengubah:", repr(teks), "->", e)
        return None
    else:
        print("Berhasil mengubah:", repr(teks))
        return angka


def baca_file(nama):
    """Membaca isi file, atau None bila file tidak ada."""
    try:
        with open(nama, "r", encoding="utf-8") as berkas:
            isi = berkas.read()
    except FileNotFoundError:
        print("File tidak ditemukan:", nama)
        return None
    return isi


def main():
    """Alur utama program."""
    print(ke_angka("42"))
    print(ke_angka("abc"))
    print(baca_file("tidak_ada.txt"))
    print("Program tetap berjalan sampai akhir")


if __name__ == "__main__":
    main()
