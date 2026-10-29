#!/usr/bin/env python3
"""Parameter __init__: wajib, opsional, keyword, dan validasi."""


class Buku:
    """Cetakan buku perpustakaan."""

    def __init__(self, judul, penulis, halaman, tersedia=True):
        if not judul.strip():
            raise ValueError("judul tidak boleh kosong")
        if halaman <= 0:
            raise ValueError("halaman harus lebih dari 0")
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman
        self.tersedia = tersedia


def main():
    """Alur utama program."""
    buku1 = Buku("Python Dasar", "Andi", 250)
    print("buku1 dibuat:", vars(buku1))

    buku2 = Buku(halaman=180, penulis="Sari", judul="Belajar OOP")
    print("buku2 dibuat:", vars(buku2))

    try:
        Buku("Rusak", "Budi", -5)
    except ValueError as e:
        print("Ditolak:", e)

    try:
        Buku("Tanpa Halaman", "Budi")
    except TypeError as e:
        print("TypeError:", e)


if __name__ == "__main__":
    main()
