#!/usr/bin/env python3
"""Mendefinisikan kelas: kerangka dasar dan urutan eksekusinya."""


class Buku:
    """Cetakan buku perpustakaan."""

    print("Tubuh kelas Buku dijalankan")

    def __init__(self, judul):
        self.judul = judul


def main():
    """Alur utama program."""
    print("main() mulai")
    buku1 = Buku("Python Dasar")
    buku2 = Buku("Belajar OOP")
    print("buku1:", buku1.judul)
    print("buku2:", buku2.judul)
    print("Nama kelas:", Buku.__name__)
    print("Docstring :", Buku.__doc__)


if __name__ == "__main__":
    main()
