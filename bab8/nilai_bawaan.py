#!/usr/bin/env python3
"""Jebakan nilai bawaan list pada parameter __init__."""


class AnggotaRawan:
    """Versi SALAH: nilai bawaan berupa list."""

    def __init__(self, nama, pinjaman=[]):
        self.nama = nama
        self.pinjaman = pinjaman

    def pinjam(self, judul):
        """Tambahkan judul ke daftar pinjaman."""
        self.pinjaman.append(judul)


class Anggota:
    """Versi BENAR: nilai bawaan None, list dibuat di dalam."""

    def __init__(self, nama, pinjaman=None):
        self.nama = nama
        if pinjaman is None:
            pinjaman = []
        self.pinjaman = pinjaman

    def pinjam(self, judul):
        """Tambahkan judul ke daftar pinjaman."""
        self.pinjaman.append(judul)


def main():
    """Bandingkan versi salah dan versi benar."""
    budi = AnggotaRawan("Budi")
    sari = AnggotaRawan("Sari")
    budi.pinjam("Python Dasar")
    print("Rawan - Budi:", budi.pinjaman)
    print("Rawan - Sari:", sari.pinjaman)
    print("Rawan - satu list:", budi.pinjaman is sari.pinjaman)

    print("-" * 30)

    andi = Anggota("Andi")
    rina = Anggota("Rina")
    andi.pinjam("Python Dasar")
    print("Benar - Andi:", andi.pinjaman)
    print("Benar - Rina:", rina.pinjaman)
    print("Benar - satu list:", andi.pinjaman is rina.pinjaman)


if __name__ == "__main__":
    main()
