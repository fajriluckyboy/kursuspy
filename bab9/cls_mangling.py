#!/usr/bin/env python3
"""Penutup polimorfisme: cls(...) dan name mangling.

Bagian 1 (cls lawan nama kelas langsung):
Rekening       : induk dengan dua konstruktor alternatif
Tabungan       : anak (jenis ditimpa, atribut kelas BUNGA_PERSEN)
Berjangka      : anak yang mewajibkan parameter tenor_bulan
BerjangkaBenar : anak Berjangka yang menimpa konstruktor alternatif

Bagian 2 (name mangling):
RekeningRapuh, TabunganRapuh : satu garis bawah, bentrok nama
RekeningAman, TabunganAman   : dua garis bawah, tidak bentrok
BiayaBiasa, TabunganBiasa    : metode _hitung, boleh ditimpa
BiayaPrivat, TabunganPrivat  : metode __hitung, tidak tertimpa
"""


class Rekening:
    """Induk dengan dua konstruktor alternatif."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def jenis(self):
        """Kembalikan nama jenis rekening."""
        return "Rekening"

    @classmethod
    def nama_pemanggil(cls):
        """Kembalikan nama kelas yang memanggil metode ini."""
        return cls.__name__

    @classmethod
    def dari_teks_kaku(cls, teks):
        """Buat objek dari teks 'nama, saldo' dengan nama kelas langsung.

        Parameter cls diterima tetapi sengaja tidak dipakai: metode ini
        hanya pembanding.
        """
        pemilik, saldo = teks.split(",")
        return Rekening(pemilik.strip(), int(saldo))

    @classmethod
    def dari_teks(cls, teks):
        """Buat objek dari teks 'nama, saldo' dengan cls."""
        pemilik, saldo = teks.split(",")
        return cls(pemilik.strip(), int(saldo))


class Tabungan(Rekening):
    """Anak biasa: tanpa __init__ sendiri."""

    BUNGA_PERSEN = 5

    def jenis(self):
        """Timpa: nama jenis Tabungan."""
        return "Tabungan"


class Berjangka(Rekening):
    """Anak yang mewajibkan parameter tenor_bulan."""

    def __init__(self, pemilik, saldo, tenor_bulan):
        super().__init__(pemilik, saldo)
        self.tenor_bulan = tenor_bulan

    def jenis(self):
        """Timpa: nama jenis Berjangka."""
        return "Berjangka"


class BerjangkaBenar(Berjangka):
    """Anak Berjangka yang menyesuaikan konstruktor alternatifnya."""

    @classmethod
    def dari_teks(cls, teks):
        """Buat objek dari teks 'nama, saldo, tenor'."""
        pemilik, saldo, tenor = teks.split(",")
        return cls(pemilik.strip(), int(saldo), int(tenor))


# ---------- Bagian 2: name mangling ----------


class RekeningRapuh:
    """Induk dengan satu garis bawah."""

    def __init__(self):
        self._catatan = []

    def catat(self, teks):
        """Tambahkan satu catatan."""
        self._catatan.append(teks)

    def jumlah_catatan(self):
        """Kembalikan jumlah catatan."""
        return len(self._catatan)


class TabunganRapuh(RekeningRapuh):
    """Anak yang memakai nama _catatan untuk hal lain."""

    def __init__(self):
        super().__init__()
        # nama sama dengan milik induk, maksudnya berbeda
        self._catatan = "promo bulan ini"


class RekeningAman:
    """Induk dengan dua garis bawah."""

    def __init__(self):
        self.__catatan = []

    def catat(self, teks):
        """Tambahkan satu catatan."""
        self.__catatan.append(teks)

    def jumlah_catatan(self):
        """Kembalikan jumlah catatan."""
        return len(self.__catatan)


class TabunganAman(RekeningAman):
    """Anak yang memakai nama __catatan untuk hal lain."""

    def __init__(self):
        super().__init__()
        # tulisan sama dengan milik induk, nama hasilnya berbeda
        self.__catatan = "promo bulan ini"

    def promo(self):
        """Kembalikan teks promo milik anak."""
        return self.__catatan


class BiayaBiasa:
    """Induk dengan metode pembantu satu garis bawah."""

    def biaya(self):
        """Biaya akhir: hasil _hitung ditambah 10."""
        return self._hitung() + 10

    def _hitung(self):
        """Biaya dasar milik induk."""
        return 100


class TabunganBiasa(BiayaBiasa):
    """Anak yang menimpa _hitung."""

    def _hitung(self):
        """Biaya dasar milik anak."""
        return 5


class BiayaPrivat:
    """Induk dengan metode pembantu dua garis bawah."""

    def biaya(self):
        """Biaya akhir: hasil __hitung ditambah 10."""
        return self.__hitung() + 10

    def __hitung(self):
        """Biaya dasar milik induk."""
        return 100


class TabunganPrivat(BiayaPrivat):
    """Anak yang menulis __hitung sendiri."""

    def __hitung(self):
        """Biaya dasar milik anak."""
        return 5


def deskripsi(obj):
    """Kembalikan nama kelas dan jenis() dari sebuah objek."""
    return f"kelas {type(obj).__name__}, jenis() = {obj.jenis()}"


def nama_berisi(kelas, kata):
    """Kembalikan nama di vars(kelas) yang memuat 'kata'."""
    hasil = []
    for nama in vars(kelas):
        if kata in nama:
            hasil.append(nama)
    return hasil


def percobaan_kaku():
    """Percobaan 1: konstruktor alternatif dengan nama kelas langsung."""
    print("== Percobaan 1: nama kelas langsung ==")
    r = Tabungan.dari_teks_kaku("Sari, 250")
    print("hasil               :", deskripsi(r))
    print("isinstance Tabungan :", isinstance(r, Tabungan))
    print("punya BUNGA_PERSEN  :", hasattr(r, "BUNGA_PERSEN"))


def percobaan_cls():
    """Percobaan 2: konstruktor alternatif dengan cls."""
    print("== Percobaan 2: cls ==")
    print("Rekening.nama_pemanggil():", Rekening.nama_pemanggil())
    print("Tabungan.nama_pemanggil():", Tabungan.nama_pemanggil())
    t = Tabungan.dari_teks("Sari, 250")
    print("hasil               :", deskripsi(t))
    print("isinstance Tabungan :", isinstance(t, Tabungan))
    print("punya BUNGA_PERSEN  :", hasattr(t, "BUNGA_PERSEN"))
    print("vars(t)             :", vars(t))
    r = Rekening.dari_teks("Budi, 100")
    print("dari Rekening       :", deskripsi(r))


def percobaan_tanda_tangan():
    """Percobaan 3: anak yang mengubah tanda tangan __init__."""
    print("== Percobaan 3: tanda tangan __init__ anak ==")
    try:
        Berjangka.dari_teks("Sari, 250")
    except TypeError as e:
        print("Berjangka.dari_teks -> TypeError:", e)
    b = BerjangkaBenar.dari_teks("Sari, 250, 12")
    print("BerjangkaBenar      :", deskripsi(b))
    print("vars(b)             :", vars(b))


def percobaan_rapuh():
    """Percobaan 4: satu garis bawah bentrok."""
    print("== Percobaan 4: satu garis bawah ==")
    t = TabunganRapuh()
    print("vars(t)        :", vars(t))
    try:
        t.catat("setor 50")
    except AttributeError as e:
        print("catat -> AttributeError:", e)


def percobaan_aman():
    """Percobaan 5: dua garis bawah tidak bentrok."""
    print("== Percobaan 5: dua garis bawah ==")
    t = TabunganAman()
    t.catat("setor 50")
    print("jumlah_catatan :", t.jumlah_catatan())
    print("promo          :", t.promo())
    print("vars(t)        :", vars(t))
    print("hasattr '__catatan'            :", hasattr(t, "__catatan"))
    print("t._RekeningAman__catatan       :", t._RekeningAman__catatan)
    try:
        t.__catatan
    except AttributeError as e:
        print("t.__catatan -> AttributeError:", e)


def percobaan_metode():
    """Percobaan 6: metode satu dan dua garis bawah."""
    print("== Percobaan 6: metode ==")
    print("TabunganBiasa().biaya()  :", TabunganBiasa().biaya())
    print("TabunganPrivat().biaya() :", TabunganPrivat().biaya())
    print("vars(BiayaPrivat)  :", nama_berisi(BiayaPrivat, "hitung"))
    print("vars(TabunganPrivat):", nama_berisi(TabunganPrivat, "hitung"))


def main():
    """Alur utama program."""
    percobaan_kaku()
    percobaan_cls()
    percobaan_tanda_tangan()
    percobaan_rapuh()
    percobaan_aman()
    percobaan_metode()


if __name__ == "__main__":
    main()
