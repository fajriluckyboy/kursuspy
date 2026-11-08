#!/usr/bin/env python3
"""Pewarisan ganda: sintaks, MRO, dan konflik nama.

Rekening      : kakek bersama (pemilik, saldo, ringkas, jenis)
Tabungan      : anak Rekening (bunga, jenis, CATATAN)
Giro          : anak Rekening (biaya admin, jenis, CATATAN)
TabunganGiro  : dua induk, urutan (Tabungan, Giro)
GiroTabungan  : dua induk, urutan (Giro, Tabungan)
"""


class Rekening:
    """Kakek bersama: aturan umum rekening."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def ringkas(self):
        """Kembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"

    def jenis(self):
        """Kembalikan nama jenis rekening."""
        return "Rekening"


class Tabungan(Rekening):
    """Induk 1: rekening berbunga."""

    BUNGA_PERSEN = 5
    CATATAN = "dari Tabungan"

    def jenis(self):
        """Override: jenis Tabungan."""
        return "Tabungan"

    def beri_bunga(self):
        """Tambahkan bunga ke saldo."""
        self.saldo += self.saldo * self.BUNGA_PERSEN / 100


class Giro(Rekening):
    """Induk 2: rekening dengan biaya admin."""

    BIAYA_ADMIN = 500
    CATATAN = "dari Giro"

    def jenis(self):
        """Override: jenis Giro."""
        return "Giro"

    def potong_admin(self):
        """Kurangi saldo dengan biaya admin."""
        self.saldo -= self.BIAYA_ADMIN


class TabunganGiro(Tabungan, Giro):
    """Anak dua induk: Tabungan ditulis lebih dulu."""


class GiroTabungan(Giro, Tabungan):
    """Anak dua induk: Giro ditulis lebih dulu."""


def nama_mro(kelas):
    """Kembalikan list nama kelas menurut urutan MRO."""
    hasil = []
    for k in kelas.__mro__:
        hasil.append(k.__name__)
    return hasil


def pemilik_nama(kelas, nama):
    """Kembalikan nama kelas pertama di MRO yang memiliki 'nama'."""
    for k in kelas.__mro__:
        if nama in vars(k):
            return k.__name__
    return None


def percobaan_mro():
    """Percobaan 1: melihat MRO."""
    print("== Percobaan 1: MRO ==")
    print("TabunganGiro :", nama_mro(TabunganGiro))
    print("GiroTabungan :", nama_mro(GiroTabungan))
    print("Tabungan     :", nama_mro(Tabungan))
    print("jenis __mro__:", type(TabunganGiro.__mro__).__name__)
    print("jenis mro()  :", type(TabunganGiro.mro()).__name__)


def percobaan_konflik():
    """Percobaan 2: konflik nama, urutan induk menentukan."""
    print("== Percobaan 2: konflik nama ==")
    a = TabunganGiro("Fajri", 1000)
    b = GiroTabungan("Fajri", 1000)
    print("a.jenis()   :", a.jenis())
    print("b.jenis()   :", b.jenis())
    print("a.CATATAN   :", a.CATATAN)
    print("b.CATATAN   :", b.CATATAN)
    print("pemilik jenis (a):", pemilik_nama(TabunganGiro, "jenis"))
    print("pemilik jenis (b):", pemilik_nama(GiroTabungan, "jenis"))
    print("'jenis' di vars(TabunganGiro):", "jenis" in vars(TabunganGiro))


def percobaan_gabung():
    """Percobaan 3: milik kedua induk terkumpul di satu objek."""
    print("== Percobaan 3: menggabung ==")
    a = TabunganGiro("Fajri", 1000)
    a.beri_bunga()
    print("setelah beri_bunga :", a.saldo)
    a.potong_admin()
    print("setelah potong_admin:", a.saldo)
    print("BUNGA_PERSEN :", a.BUNGA_PERSEN)
    print("BIAYA_ADMIN  :", a.BIAYA_ADMIN)
    print("ringkas()    :", a.ringkas())
    print("vars(a)      :", vars(a))


def percobaan_isinstance():
    """Percobaan 4: objek dikenali sebagai anak kedua induk."""
    print("== Percobaan 4: isinstance dan issubclass ==")
    a = TabunganGiro("Fajri", 1000)
    print("isinstance Tabungan :", isinstance(a, Tabungan))
    print("isinstance Giro     :", isinstance(a, Giro))
    print("isinstance Rekening :", isinstance(a, Rekening))
    print("issubclass(TabunganGiro, Giro):", issubclass(TabunganGiro, Giro))
    print("issubclass(Tabungan, Giro)    :", issubclass(Tabungan, Giro))
    print("TabunganGiro.__bases__:", TabunganGiro.__bases__)


def percobaan_mro_salah():
    """Percobaan 5: urutan induk yang melanggar aturan MRO."""
    print("== Percobaan 5: MRO tidak konsisten ==")
    try:

        class Salah(Rekening, Tabungan):
            """Induk ditulis SEBELUM anaknya sendiri."""

    except TypeError as e:
        print("TypeError:", e)


def main():
    """Alur utama program."""
    percobaan_mro()
    percobaan_konflik()
    percobaan_gabung()
    percobaan_isinstance()
    percobaan_mro_salah()


if __name__ == "__main__":
    main()
