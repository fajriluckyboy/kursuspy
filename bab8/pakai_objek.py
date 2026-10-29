#!/usr/bin/env python3
"""Membuat dan menggunakan objek dari kelas Buku."""


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
    buku2 = Buku("Python Dasar", "Andi", 250)

    print("Isi buku1:", buku1.ringkas())
    print("buku1 == buku2 :", buku1 == buku2)
    print("buku1 is buku2 :", buku1 is buku2)

    buku1.tersedia = False
    print("Setelah diubah:")
    print("buku1:", buku1.ringkas())
    print("buku2:", buku2.ringkas())

    buku3 = buku1
    buku3.halaman = 300
    print("buku3 is buku1 :", buku3 is buku1)
    print("Halaman buku1  :", buku1.halaman)


if __name__ == "__main__":
    main()
