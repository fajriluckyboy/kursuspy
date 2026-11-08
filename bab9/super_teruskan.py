#!/usr/bin/env python3
"""Meneruskan *args dan **kwargs ke __init__ induk.

TabunganEksplisit : cara Bagian A (parameter induk ditulis ulang)
TabunganTeruskan  : pola baku (full forwarding, keyword-only)
TabunganBocor     : jebakan, parameter anak bocor ke induk
"""


class Rekening:
    """Kelas induk: sekarang punya tiga parameter."""

    def __init__(self, pemilik, saldo=0, bank="Bank Kursus"):
        if saldo < 0:
            raise ValueError("saldo tidak boleh negatif")
        self.pemilik = pemilik
        self.saldo = saldo
        self.bank = bank


class TabunganEksplisit(Rekening):
    """Cara Bagian A: hanya mengenal pemilik dan saldo."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5):
        super().__init__(pemilik, saldo)
        self.bunga_persen = bunga_persen


class TabunganTeruskan(Rekening):
    """Pola baku: menampung sisa argumen dan meneruskannya ke induk.

    Diterima  : apa pun milik Rekening, ditambah bunga_persen
                (hanya dengan nama).
    Diteruskan: semuanya, kecuali bunga_persen.
    """

    def __init__(self, *args, bunga_persen=5, **kwargs):
        super().__init__(*args, **kwargs)
        self.bunga_persen = bunga_persen


class TabunganBocor(Rekening):
    """JEBAKAN: bunga_persen tidak dikeluarkan dari kwargs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bunga_persen = kwargs["bunga_persen"]


def tampil(a, b, c=0, **sisa):
    """Pengamatan membongkar: cetak apa yang diterima."""
    print("  a, b, c =", a, b, c, "| sisa =", sisa)


def percobaan_bongkar():
    """Percobaan 1: * dan ** saat memanggil."""
    print("== Percobaan 1: membongkar ==")
    daftar = [1, 2, 3]
    kamus = {"x": 10, "y": 20}
    tampil(*daftar)
    tampil(*daftar[:2], **kamus)
    tampil(1, 2, 3, x=10, y=20)


def percobaan_induk_berubah():
    """Percobaan 2: induk punya parameter baru bernama bank."""
    print("== Percobaan 2: induk bertambah parameter ==")
    try:
        TabunganEksplisit("Fajri", 100, bank="Bank Baru")
    except TypeError as e:
        print("Eksplisit : TypeError:", e)

    t = TabunganTeruskan("Fajri", 100, bank="Bank Baru", bunga_persen=7)
    print("Teruskan  :", vars(t))


def percobaan_default():
    """Percobaan 3: berbagai cara memanggil pola baku."""
    print("== Percobaan 3: cara memanggil ==")
    print("hanya pemilik     :", vars(TabunganTeruskan("Sari")))
    print("dengan bunga      :", vars(TabunganTeruskan("Sari", bunga_persen=3)))
    print("saldo lewat nama  :", vars(TabunganTeruskan(pemilik="Sari", saldo=50)))


def percobaan_posisi():
    """Percobaan 4: bunga_persen tidak bisa diisi secara posisi."""
    print("== Percobaan 4: bunga secara posisi ==")
    try:
        TabunganTeruskan("Fajri", 100, "Bank Baru", 7)
    except TypeError as e:
        print("TypeError:", e)


def percobaan_bocor():
    """Percobaan 5: jebakan parameter bocor ke induk."""
    print("== Percobaan 5: bocor ke induk ==")
    try:
        TabunganBocor("Fajri", 100, bunga_persen=7)
    except TypeError as e:
        print("TypeError:", e)


def percobaan_induk_menolak():
    """Percobaan 6: pemeriksaan induk tetap berlaku."""
    print("== Percobaan 6: induk menolak ==")
    try:
        TabunganTeruskan("Rusak", -5)
    except ValueError as e:
        print("ValueError:", e)


def main():
    """Alur utama program."""
    percobaan_bongkar()
    percobaan_induk_berubah()
    percobaan_default()
    percobaan_posisi()
    percobaan_bocor()
    percobaan_induk_menolak()


if __name__ == "__main__":
    main()
