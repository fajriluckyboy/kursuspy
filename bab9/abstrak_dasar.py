#!/usr/bin/env python3
"""Kelas abstrak dan metode abstrak (modul abc).

Rekening        : kelas abstrak (jenis dan biaya_bulanan wajib diisi)
Tabungan, Giro  : anak lengkap
GiroLupa        : anak yang lupa mengisi biaya_bulanan
GiroSalahKetik  : anak yang salah ketik nama biaya_bulanan
"""

from abc import ABC, abstractmethod


class Rekening(ABC):
    """Kerangka semua rekening. Tidak dibuat objeknya langsung."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    @abstractmethod
    def jenis(self):
        """Kembalikan nama jenis rekening (teks). WAJIB diisi anak."""

    @abstractmethod
    def biaya_bulanan(self):
        """Kembalikan biaya bulanan (angka). WAJIB diisi anak."""

    def tutup_bulan(self):
        """Potong biaya bulanan dari saldo, kembalikan saldo baru."""
        self.saldo -= self.biaya_bulanan()
        return self.saldo


class Tabungan(Rekening):
    """Anak lengkap: tanpa biaya bulanan."""

    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Tabungan"

    def biaya_bulanan(self):
        """Isi kontrak: tabungan tidak berbiaya."""
        return 0


class Giro(Rekening):
    """Anak lengkap: berbiaya admin tetap."""

    BIAYA_ADMIN = 500

    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Giro"

    def biaya_bulanan(self):
        """Isi kontrak: biaya admin tetap."""
        return self.BIAYA_ADMIN


class GiroLupa(Rekening):
    """Anak tidak lengkap: hanya mengisi jenis."""

    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "GiroLupa"


class GiroSalahKetik(Rekening):
    """Anak tidak lengkap: nama metode kedua salah ketik."""

    BIAYA_ADMIN = 500

    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "GiroSalahKetik"

    def biaya_bulan(self):
        """Salah ketik: seharusnya biaya_bulanan."""
        return self.BIAYA_ADMIN


def nama_mro(kelas):
    """Kembalikan list nama kelas menurut urutan MRO."""
    hasil = []
    for k in kelas.__mro__:
        hasil.append(k.__name__)
    return hasil


def percobaan_langsung():
    """Percobaan 1: kelas abstrak dibuat langsung."""
    print("== Percobaan 1: kelas abstrak dibuat langsung ==")
    try:
        Rekening("Fajri", 1000)
    except TypeError as e:
        print("TypeError:", e)


def percobaan_lengkap():
    """Percobaan 2: anak lengkap."""
    print("== Percobaan 2: anak lengkap ==")
    t = Tabungan("Fajri", 1000)
    g = Giro("Sari", 1000)
    print("t.jenis()        :", t.jenis())
    print("g.jenis()        :", g.jenis())
    print("t.biaya_bulanan():", t.biaya_bulanan())
    print("g.biaya_bulanan():", g.biaya_bulanan())
    print("t.tutup_bulan()  :", t.tutup_bulan())
    print("g.tutup_bulan()  :", g.tutup_bulan())
    print("vars(t)          :", vars(t))


def percobaan_tidak_lengkap():
    """Percobaan 3: anak lupa mengisi dan anak salah ketik."""
    print("== Percobaan 3: anak tidak lengkap ==")
    print("Kelas sudah terdefinisi:", GiroLupa.__name__, GiroSalahKetik.__name__)
    for kelas in (GiroLupa, GiroSalahKetik):
        print("--", kelas.__name__, "--")
        try:
            kelas("Fajri", 1000)
        except TypeError as e:
            print("TypeError:", e)
    print("hasattr biaya_bulan  :", hasattr(GiroSalahKetik, "biaya_bulan"))
    print("hasattr biaya_bulanan:", hasattr(GiroSalahKetik, "biaya_bulanan"))


def percobaan_abstractmethods():
    """Percobaan 4: isi __abstractmethods__ tiap kelas."""
    print("== Percobaan 4: __abstractmethods__ ==")
    for kelas in (Rekening, Tabungan, GiroLupa, GiroSalahKetik):
        print(f"{kelas.__name__:15}:", sorted(kelas.__abstractmethods__))
    print("tipe           :", type(Rekening.__abstractmethods__).__name__)


def percobaan_hubungan():
    """Percobaan 5: hubungan kelas abstrak dengan anak dan MRO."""
    print("== Percobaan 5: hubungan ==")
    t = Tabungan("Fajri", 1000)
    print("MRO Tabungan           :", nama_mro(Tabungan))
    print("bases Rekening         :", Rekening.__bases__)
    print("isinstance(t, Rekening):", isinstance(t, Rekening))
    print("isinstance(t, ABC)     :", isinstance(t, ABC))
    print("issubclass(Giro, Rekening):", issubclass(Giro, Rekening))


def main():
    """Alur utama program."""
    percobaan_langsung()
    percobaan_lengkap()
    percobaan_tidak_lengkap()
    percobaan_abstractmethods()
    percobaan_hubungan()


if __name__ == "__main__":
    main()
