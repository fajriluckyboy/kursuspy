#!/usr/bin/env python3
"""Pewarisan dasar: kelas anak memakai kode kelas induk.

Induk : Rekening
Anak  : Tabungan (isinya hanya 'pass', tidak menulis ulang apa pun)
"""


class Rekening:
    """Kelas induk: rekening bank umum."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        """Tambah saldo."""
        self.saldo += jumlah

    def ringkas(self):
        """Kembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"


class Tabungan(Rekening):
    """Kelas anak: mewarisi semua milik Rekening."""

    # 'pass' = tubuh kelas kosong; anak tetap lengkap berkat induk
    pass


def main():
    """Alur utama program."""
    t = Tabungan("Fajri", 100)

    print("--- Anak memakai kode induk ---")
    t.setor(50)
    print("ringkas()           :", t.ringkas())
    print("vars(t)             :", vars(t))

    print("--- Memeriksa hubungan ---")
    print("type(t)             :", type(t))
    print("isinstance(t, Tabungan):", isinstance(t, Tabungan))
    print("isinstance(t, Rekening):", isinstance(t, Rekening))
    print("issubclass(Tabungan, Rekening):", issubclass(Tabungan, Rekening))
    print("issubclass(Rekening, Tabungan):", issubclass(Rekening, Tabungan))
    print("Tabungan.__bases__  :", Tabungan.__bases__)
    print("Rekening.__bases__  :", Rekening.__bases__)

    print("--- Induk tidak mewarisi dari anak ---")
    r = Rekening("Sari", 10)
    print("isinstance(r, Tabungan):", isinstance(r, Tabungan))


if __name__ == "__main__":
    main()
