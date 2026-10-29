#!/usr/bin/env python3
"""Objek dalam koleksi, fungsi penerima objek, hasattr dan vars."""


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


def pinjam(buku):
    """Tandai buku sebagai dipinjam."""
    buku.tersedia = False


def hitung_tersedia(daftar):
    """Kembalikan jumlah buku yang masih tersedia."""
    jumlah = 0
    for buku in daftar:
        if buku.tersedia:
            jumlah += 1
    return jumlah


def main():
    """Alur utama program."""
    rak = [
        Buku("Python Dasar", "Andi", 250),
        Buku("Belajar OOP", "Sari", 180),
        Buku("Struktur Data", "Budi", 320),
    ]

    print("Isi rak:")
    for buku in rak:
        print("-", buku.ringkas())

    print("Tersedia sebelum pinjam:", hitung_tersedia(rak))
    pinjam(rak[1])
    print("Tersedia sesudah pinjam:", hitung_tersedia(rak))
    print("rak[1]:", rak[1].ringkas())

    buku = rak[0]
    print("Punya atribut judul   :", hasattr(buku, "judul"))
    print("Punya atribut penerbit:", hasattr(buku, "penerbit"))
    print("Isi atribut buku      :", vars(buku))


if __name__ == "__main__":
    main()
