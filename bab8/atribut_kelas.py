#!/usr/bin/env python3
"""Atribut kelas (statis) dibandingkan dengan atribut objek.

Atribut kelas : BANK dan jumlah, satu salinan dipakai bersama.
Atribut objek : pemilik, satu salinan per objek.
"""


class Rekening:
    """Rekening bank dengan atribut kelas bersama."""

    # Atribut kelas: ditulis di tubuh kelas, di luar metode.
    # Dibuat SEKALI saat kelas didefinisikan.
    BANK = "Bank Kursus"
    jumlah = 0

    def __init__(self, pemilik):
        # Atribut objek: tiap objek punya salinan sendiri
        self.pemilik = pemilik
        # Ubah atribut kelas lewat NAMA KELAS, bukan self.
        # Kalau ditulis self.jumlah += 1, Python membuat atribut
        # objek baru (membayangi), dan penghitung kelas tidak naik.
        Rekening.jumlah += 1


def main():
    """Alur utama program."""
    r1 = Rekening("Fajri")
    r2 = Rekening("Sari")

    print("--- Dibaca lewat kelas dan objek ---")
    print("Rekening.BANK   :", Rekening.BANK)
    print("r1.BANK         :", r1.BANK)
    print("r2.BANK         :", r2.BANK)
    print("Jumlah rekening :", Rekening.jumlah)

    print("--- Isi objek (vars) ---")
    # BANK dan jumlah tidak ada di sini, karena milik kelas
    print("vars(r1)        :", vars(r1))

    print("--- Ubah lewat kelas ---")
    Rekening.BANK = "Bank Baru"
    print("r1.BANK         :", r1.BANK)
    print("r2.BANK         :", r2.BANK)

    print("--- Ubah lewat objek (membayangi) ---")
    r1.BANK = "Bank Khusus"
    print("r1.BANK         :", r1.BANK)
    print("r2.BANK         :", r2.BANK)
    print("Rekening.BANK   :", Rekening.BANK)
    print("vars(r1)        :", vars(r1))


if __name__ == "__main__":
    main()
