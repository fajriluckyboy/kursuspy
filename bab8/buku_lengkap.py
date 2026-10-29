#!/usr/bin/env python3
"""Kelas Buku dengan beberapa atribut dan satu metode."""


class Buku:
    """Cetakan buku perpustakaan."""

    def __init__(self, judul, penulis, halaman, tersedia=True):
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman
        self.tersedia = tersedia

    def ringkas(self):
        """Kembalikan satu kalimat ringkasan buku."""
        status = "tersedia" if self.tersedia else "dipinjam"
        return f"{self.judul} oleh {self.penulis}, {self.halaman} hlm ({status})"


def main():
    """Alur utama program."""
    buku1 = Buku("Python Dasar", "Andi", 250)
    buku2 = Buku("Belajar OOP", "Sari", 180, tersedia=False)
    print(buku1.ringkas())
    print(buku2.ringkas())
    print("Halaman buku2:", buku2.halaman)


if __name__ == "__main__":
    main()
