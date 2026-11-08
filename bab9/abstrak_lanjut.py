#!/usr/bin/env python3
"""Kelas abstrak lanjutan: kode di metode abstrak, properti abstrak,
ABC tanpa metode abstrak, dan kelas abstrak bertingkat.

Rekening         : abstrak (jenis = properti, biaya_bulanan berisi kode)
Tabungan, Giro   : anak lengkap, memakai isi induk lewat super()
TabunganMalas    : hanya mengisi jenis
GiroJenisBiasa   : mengisi jenis dengan metode biasa (jebakan)
Pencetak         : berinduk ABC tanpa metode abstrak
RekeningBerbunga : tingkat tengah, masih abstrak
TabunganBerbunga : ujung, konkret
DepositoLupa     : anak tingkat tengah yang kurang lengkap
"""

from abc import ABC, abstractmethod


class Rekening(ABC):
    """Kerangka semua rekening."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    @property
    @abstractmethod
    def jenis(self):
        """Nama jenis rekening (properti). WAJIB diisi anak."""

    @abstractmethod
    def biaya_bulanan(self):
        """Biaya bulanan. WAJIB ditimpa anak.

        Berisi biaya dasar 100 yang boleh dipakai anak lewat super().
        """
        return 100

    def tutup_bulan(self):
        """Potong biaya bulanan dari saldo, kembalikan saldo baru."""
        self.saldo -= self.biaya_bulanan()
        return self.saldo


class Tabungan(Rekening):
    """Anak lengkap: memakai biaya dasar induk apa adanya."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Tabungan"

    def biaya_bulanan(self):
        """Isi kontrak: biaya dasar dari induk."""
        return super().biaya_bulanan()


class Giro(Rekening):
    """Anak lengkap: biaya dasar induk ditambah biaya admin."""

    BIAYA_ADMIN = 400

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "Giro"

    def biaya_bulanan(self):
        """Isi kontrak: biaya dasar induk + biaya admin."""
        return super().biaya_bulanan() + self.BIAYA_ADMIN


class TabunganMalas(Rekening):
    """Anak tidak lengkap: tidak menimpa biaya_bulanan."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "TabunganMalas"


class GiroJenisBiasa(Rekening):
    """JEBAKAN: jenis diisi metode biasa, bukan properti."""

    def jenis(self):
        """Metode biasa, bukan properti."""
        return "Giro"

    def biaya_bulanan(self):
        """Isi kontrak: biaya dasar induk + 400."""
        return super().biaya_bulanan() + 400


class Pencetak(ABC):
    """Berinduk ABC, tetapi tanpa metode abstrak."""

    def cetak(self, teks):
        """Kembalikan teks berlabel."""
        return f"[cetak] {teks}"


class RekeningBerbunga(Rekening):
    """Tingkat tengah: mengisi biaya, menambah kontrak bunga."""

    def biaya_bulanan(self):
        """Isi kontrak: rekening berbunga bebas biaya."""
        return 0

    @abstractmethod
    def bunga_persen(self):
        """Persentase bunga (angka). WAJIB diisi anak."""

    def beri_bunga(self):
        """Tambahkan bunga ke saldo, kembalikan jumlah bunga."""
        tambahan = self.saldo * self.bunga_persen() / 100
        self.saldo += tambahan
        return tambahan


class TabunganBerbunga(RekeningBerbunga):
    """Ujung: semua kontrak terisi."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "TabunganBerbunga"

    def bunga_persen(self):
        """Isi kontrak: bunga 5 persen."""
        return 5


class DepositoLupa(RekeningBerbunga):
    """Anak tingkat tengah: lupa mengisi bunga_persen."""

    @property
    def jenis(self):
        """Isi kontrak: nama jenis."""
        return "DepositoLupa"


def nama_mro(kelas):
    """Kembalikan list nama kelas menurut urutan MRO."""
    hasil = []
    for k in kelas.__mro__:
        hasil.append(k.__name__)
    return hasil


def percobaan_super():
    """Percobaan 1: metode abstrak yang berisi kode."""
    print("== Percobaan 1: metode abstrak berisi kode ==")
    t = Tabungan("Fajri", 1000)
    g = Giro("Sari", 1000)
    print("Rekening.biaya_bulanan(t):", Rekening.biaya_bulanan(t))
    print("t.biaya_bulanan()        :", t.biaya_bulanan())
    print("g.biaya_bulanan()        :", g.biaya_bulanan())
    print("t.tutup_bulan()          :", t.tutup_bulan())
    print("g.tutup_bulan()          :", g.tutup_bulan())


def percobaan_malas():
    """Percobaan 2: induk berisi kode, anak tetap wajib menimpa."""
    print("== Percobaan 2: induk berisi kode, anak tetap wajib ==")
    print("abstractmethods:", sorted(TabunganMalas.__abstractmethods__))
    try:
        TabunganMalas("Fajri", 1000)
    except TypeError as e:
        print("TypeError:", e)


def percobaan_properti():
    """Percobaan 3: properti abstrak dan jebakan metode biasa."""
    print("== Percobaan 3: properti abstrak ==")
    t = Tabungan("Fajri", 1000)
    print("t.jenis                :", t.jenis)
    print("tipe t.jenis           :", type(t.jenis).__name__)
    print("Rekening.jenis property:", isinstance(Rekening.jenis, property))
    print("-- jebakan: diisi metode biasa --")
    r = GiroJenisBiasa("Sari", 1000)
    print("objek berhasil dibuat  :", r.pemilik)
    print("abstractmethods        :", sorted(GiroJenisBiasa.__abstractmethods__))
    print("tipe r.jenis           :", type(r.jenis).__name__)
    print("r.jenis()              :", r.jenis())


def percobaan_tanpa_abstrak():
    """Percobaan 4: berinduk ABC tanpa metode abstrak."""
    print("== Percobaan 4: ABC tanpa metode abstrak ==")
    p = Pencetak()
    print("objek dibuat   :", type(p).__name__)
    print("abstractmethods:", sorted(Pencetak.__abstractmethods__))
    print("p.cetak        :", p.cetak("halo"))
    print("isinstance ABC :", isinstance(p, ABC))


def percobaan_bertingkat():
    """Percobaan 5: kelas abstrak bertingkat."""
    print("== Percobaan 5: bertingkat ==")
    semua = (Rekening, RekeningBerbunga, TabunganBerbunga, DepositoLupa)
    for kelas in semua:
        print(f"{kelas.__name__:17}:", sorted(kelas.__abstractmethods__))
    for kelas in (RekeningBerbunga, DepositoLupa):
        print("--", kelas.__name__, "--")
        try:
            kelas("Fajri", 1000)
        except TypeError as e:
            print("TypeError:", e)
    b = TabunganBerbunga("Fajri", 1000)
    print("jenis       :", b.jenis)
    print("beri_bunga  :", b.beri_bunga())
    print("saldo       :", b.saldo)
    print("tutup_bulan :", b.tutup_bulan())
    print("MRO         :", nama_mro(TabunganBerbunga))


def main():
    """Alur utama program."""
    percobaan_super()
    percobaan_malas()
    percobaan_properti()
    percobaan_tanpa_abstrak()
    percobaan_bertingkat()


if __name__ == "__main__":
    main()
