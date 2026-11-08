#!/usr/bin/env python3
"""Polimorfisme: satu kode, banyak jenis objek.

Rekening (abstrak) : antarmuka jenis dan biaya_bulanan()
Tabungan, Giro,
Deposito           : anak Rekening (polimorfisme lewat pewarisan)
Dompet             : BUKAN anak Rekening, tetapi punya antarmuka
                     yang sama (duck typing)
Brankas            : tidak punya biaya_bulanan()
"""

from abc import ABC, abstractmethod


class Rekening(ABC):
    """Kerangka rekening: menetapkan antarmuka."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    @property
    @abstractmethod
    def jenis(self):
        """Nama jenis rekening (properti). WAJIB diisi anak."""

    @abstractmethod
    def biaya_bulanan(self):
        """Biaya bulanan (angka). WAJIB diisi anak."""


class Tabungan(Rekening):
    """Rekening tanpa biaya."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Tabungan"

    def biaya_bulanan(self):
        """Isi kontrak: gratis."""
        return 0


class Giro(Rekening):
    """Rekening dengan biaya admin tetap."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Giro"

    def biaya_bulanan(self):
        """Isi kontrak: biaya admin 500."""
        return 500


class Deposito(Rekening):
    """Jenis baru: ditambahkan tanpa mengubah kode umum."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Deposito"

    def biaya_bulanan(self):
        """Isi kontrak: biaya 250."""
        return 250


class Dompet:
    """BUKAN anak Rekening. Hanya kebetulan punya antarmuka sama."""

    jenis = "Dompet"

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def biaya_bulanan(self):
        """Biaya pemeliharaan dompet: 150."""
        return 150


class Brankas:
    """Tidak punya biaya_bulanan(): antarmukanya tidak lengkap."""

    jenis = "Brankas"


def laporan_biaya(daftar):
    """KODE UMUM: kembalikan list baris laporan biaya tiap objek."""
    baris = []
    for obj in daftar:
        baris.append(f"  {obj.jenis:9}: {obj.biaya_bulanan()}")
    return baris


def total_biaya(daftar):
    """KODE UMUM: jumlahkan biaya bulanan semua objek di daftar."""
    total = 0
    for obj in daftar:
        total += obj.biaya_bulanan()
    return total


def biaya_kaku(obj):
    """Pembanding: percabangan jenis (anti-pola)."""
    if isinstance(obj, Tabungan):
        return 0
    elif isinstance(obj, Giro):
        return 500
    else:
        raise TypeError(f"jenis tidak dikenal: {type(obj).__name__}")


def percobaan_bawaan():
    """Percobaan 1: polimorfisme pada fungsi dan operator bawaan."""
    print("== Percobaan 1: polimorfisme bawaan ==")
    for isi in ("abc", [1, 2], {"a": 1}, range(5)):
        print(f"len pada {type(isi).__name__:6}:", len(isi))
    print("1 + 2     :", 1 + 2)
    print("'a' + 'b' :", "a" + "b")
    print("[1] + [2] :", [1] + [2])


def percobaan_pewarisan():
    """Percobaan 2: satu kode, banyak jenis (termasuk bukan anak)."""
    print("== Percobaan 2: satu kode, banyak jenis ==")
    daftar = [
        Tabungan("Fajri", 1000),
        Giro("Sari", 2000),
        Dompet("Budi", 300),
    ]
    for baris in laporan_biaya(daftar):
        print(baris)
    print("total biaya:", total_biaya(daftar))
    print("isinstance(daftar[2], Rekening):", isinstance(daftar[2], Rekening))


def percobaan_tambah_jenis():
    """Percobaan 3: menambah jenis baru."""
    print("== Percobaan 3: menambah jenis baru ==")
    d = Deposito("Fajri", 5000)
    print("kode umum  :", total_biaya([d]))
    print("Tabungan lewat biaya_kaku:", biaya_kaku(Tabungan("Sari")))
    try:
        biaya_kaku(d)
    except TypeError as e:
        print("biaya_kaku(Deposito) -> TypeError:", e)


def percobaan_duck_typing():
    """Percobaan 4: duck typing dan batasnya."""
    print("== Percobaan 4: duck typing dan batasnya ==")
    print("issubclass(Dompet, Rekening)  :", issubclass(Dompet, Rekening))
    print(
        "hasattr(Dompet(...), 'biaya_bulanan') :",
        hasattr(Dompet("Budi"), "biaya_bulanan"),
    )
    print(
        "hasattr(Brankas(), 'biaya_bulanan')   :", hasattr(Brankas(), "biaya_bulanan")
    )
    try:
        total_biaya([Tabungan("Fajri", 100), Brankas()])
    except AttributeError as e:
        print("AttributeError:", e)


def main():
    """Alur utama program."""
    percobaan_bawaan()
    percobaan_pewarisan()
    percobaan_tambah_jenis()
    percobaan_duck_typing()


if __name__ == "__main__":
    main()
