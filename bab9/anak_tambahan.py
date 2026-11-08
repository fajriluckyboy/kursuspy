#!/usr/bin/env python3
"""Mendefinisikan kelas anak: tambahan milik anak sendiri.

Induk  : Rekening  (setor, ringkas)
Anak 1 : Tabungan  (tambah BUNGA_PERSEN dan beri_bunga)
Anak 2 : Giro      (tambah BIAYA_ADMIN dan potong_admin)
"""


class Rekening:
    """Kelas induk: milik bersama semua jenis rekening."""

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
    """Anak 1: rekening yang berbunga."""

    # Atribut kelas milik anak: tidak ada di Rekening
    BUNGA_PERSEN = 5

    def beri_bunga(self):
        """Tambah saldo sebesar BUNGA_PERSEN persen dari saldo."""
        # self.saldo milik objek (diisi __init__ induk)
        # self.BUNGA_PERSEN dicari: objek -> Tabungan (ketemu)
        self.saldo += self.saldo * self.BUNGA_PERSEN / 100


class Giro(Rekening):
    """Anak 2: rekening dengan biaya administrasi."""

    # Atribut kelas milik anak: tidak ada di Rekening
    BIAYA_ADMIN = 5000

    def potong_admin(self):
        """Kurangi saldo sebesar BIAYA_ADMIN."""
        self.saldo -= self.BIAYA_ADMIN


def main():
    """Alur utama program."""
    t = Tabungan("Fajri", 1000)
    g = Giro("Sari", 20000)

    print("--- Anak memakai milik induk ---")
    t.setor(500)
    print("t.ringkas()                 :", t.ringkas())

    print("--- Anak memakai tambahan sendiri ---")
    t.beri_bunga()
    print("t.ringkas()                 :", t.ringkas())
    g.potong_admin()
    print("g.ringkas()                 :", g.ringkas())

    print("--- Atribut kelas milik anak ---")
    print("Tabungan.BUNGA_PERSEN       :", Tabungan.BUNGA_PERSEN)
    print("'BUNGA_PERSEN' in vars(Tabungan):", "BUNGA_PERSEN" in vars(Tabungan))
    print("'BUNGA_PERSEN' in vars(Rekening):", "BUNGA_PERSEN" in vars(Rekening))
    print("'BUNGA_PERSEN' in vars(t)   :", "BUNGA_PERSEN" in vars(t))

    print("--- Tambahan anak tidak naik ke induk ---")
    r = Rekening("Budi", 100)
    print("hasattr(r, 'beri_bunga')    :", hasattr(r, "beri_bunga"))
    print("hasattr(t, 'beri_bunga')    :", hasattr(t, "beri_bunga"))

    print("--- Saudara tidak saling tahu ---")
    print("hasattr(t, 'potong_admin')  :", hasattr(t, "potong_admin"))
    print("hasattr(g, 'beri_bunga')    :", hasattr(g, "beri_bunga"))
    try:
        t.potong_admin()
    except AttributeError as e:
        print("AttributeError:", e)


if __name__ == "__main__":
    main()
