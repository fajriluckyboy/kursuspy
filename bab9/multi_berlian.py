#!/usr/bin/env python3
"""Pewarisan ganda: berlian, super() kooperatif, dan mixin.

Percobaan 1: berlian, induk dipanggil lewat nama (tidak baku).
Percobaan 2: berlian, rantai super() kooperatif.
Percobaan 3: urutan induk dibalik, dan Tabungan berdiri sendiri.
Percobaan 4: mixin di kiri induk utama.
Percobaan 5: mixin salah tempat dan mixin sendirian.
"""


class Rekening:
    """Akar rantai: mengambil argumen eksplisit, tidak meneruskan."""

    def __init__(self, pemilik, saldo=0):
        # print hanya alat pengamatan: menunjukkan kapan kakek jalan
        print("  Rekening.__init__ jalan")
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        """Tambahkan jumlah ke saldo."""
        self.saldo += jumlah


# ---------- Cara lewat nama (TIDAK baku, hanya untuk dikenali) ----------


class TabunganNama(Rekening):
    """Memanggil kakek lewat nama."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5):
        print("  TabunganNama.__init__ mulai")
        Rekening.__init__(self, pemilik, saldo)
        self.bunga_persen = bunga_persen


class GiroNama(Rekening):
    """Memanggil kakek lewat nama."""

    def __init__(self, pemilik, saldo=0, biaya_admin=500):
        print("  GiroNama.__init__ mulai")
        Rekening.__init__(self, pemilik, saldo)
        self.biaya_admin = biaya_admin


class TabunganGiroNama(TabunganNama, GiroNama):
    """Memanggil kedua induk lewat nama."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5, biaya_admin=500):
        TabunganNama.__init__(self, pemilik, saldo, bunga_persen)
        GiroNama.__init__(self, pemilik, saldo, biaya_admin)


# ---------- Cara baku: rantai super() kooperatif ----------


class Tabungan(Rekening):
    """Mata rantai: mengambil bunga_persen, meneruskan sisanya.

    Diterima  : argumen Rekening dan kelas lain di rantai,
                ditambah bunga_persen (hanya dengan nama).
    Diteruskan: semuanya, kecuali bunga_persen.
    """

    def __init__(self, *args, bunga_persen=5, **kwargs):
        print("  Tabungan.__init__ mulai")
        super().__init__(*args, **kwargs)
        print("  Tabungan.__init__ selesai")
        self.bunga_persen = bunga_persen


class Giro(Rekening):
    """Mata rantai: mengambil biaya_admin, meneruskan sisanya.

    Diterima  : argumen Rekening dan kelas lain di rantai,
                ditambah biaya_admin (hanya dengan nama).
    Diteruskan: semuanya, kecuali biaya_admin.
    """

    def __init__(self, *args, biaya_admin=500, **kwargs):
        print("  Giro.__init__ mulai")
        super().__init__(*args, **kwargs)
        print("  Giro.__init__ selesai")
        self.biaya_admin = biaya_admin


class TabunganGiro(Tabungan, Giro):
    """Dua induk; tanpa __init__ sendiri, rantai tetap jalan."""


class GiroTabungan(Giro, Tabungan):
    """Dua induk dengan urutan dibalik."""


# ---------- Mixin ----------


class RiwayatMixin:
    """Mixin: mencatat setoran. Bekerja sama lewat super().

    Harus ditulis di KIRI induk utama dan tidak dibuat sendirian.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.riwayat = []

    def setor(self, jumlah):
        """Setor lewat kelas berikutnya di rantai, lalu catat."""
        super().setor(jumlah)
        self.riwayat.append(f"setor {jumlah}")


class TabunganBerRiwayat(RiwayatMixin, Tabungan):
    """Mixin di kiri: miliknya didahulukan."""


class GiroBerRiwayat(RiwayatMixin, Giro):
    """Mixin yang sama dipakai pada kelas lain."""


class TabunganMixinSalah(Tabungan, RiwayatMixin):
    """JEBAKAN: mixin ditulis di kanan induk utama."""


def nama_mro(kelas):
    """Kembalikan list nama kelas menurut urutan MRO."""
    hasil = []
    for k in kelas.__mro__:
        hasil.append(k.__name__)
    return hasil


def percobaan_nama():
    """Percobaan 1: berlian, induk dipanggil lewat nama."""
    print("== Percobaan 1: berlian lewat nama ==")
    t = TabunganGiroNama("Fajri", 1000)
    print("vars(t):", vars(t))


def percobaan_kooperatif():
    """Percobaan 2: berlian, rantai super() kooperatif."""
    print("== Percobaan 2: rantai kooperatif ==")
    print("MRO    :", nama_mro(TabunganGiro))
    t = TabunganGiro("Fajri", 1000, bunga_persen=7, biaya_admin=300)
    print("vars(t):", vars(t))


def percobaan_urutan():
    """Percobaan 3: urutan dibalik dan objek Tabungan murni."""
    print("== Percobaan 3: urutan dan objek lain ==")
    print("MRO    :", nama_mro(GiroTabungan))
    g = GiroTabungan("Fajri", 1000, bunga_persen=7, biaya_admin=300)
    print("vars(g):", vars(g))
    print("-- Tabungan berdiri sendiri --")
    t = Tabungan("Sari", 100)
    print("vars(t):", vars(t))


def percobaan_mixin():
    """Percobaan 4: mixin di kiri induk utama."""
    print("== Percobaan 4: mixin ==")
    print("MRO    :", nama_mro(TabunganBerRiwayat))
    b = TabunganBerRiwayat("Fajri", 100, bunga_persen=7)
    b.setor(50)
    b.setor(25)
    print("saldo  :", b.saldo)
    print("riwayat:", b.riwayat)
    print("vars(b):", vars(b))
    g = GiroBerRiwayat("Sari", 200, biaya_admin=300)
    g.setor(10)
    print("Giro riwayat:", g.riwayat)


def percobaan_mixin_salah():
    """Percobaan 5: mixin di kanan, dan mixin sendirian."""
    print("== Percobaan 5: mixin bermasalah ==")
    print("MRO    :", nama_mro(TabunganMixinSalah))
    s = TabunganMixinSalah("Fajri", 100)
    s.setor(50)
    print("saldo  :", s.saldo)
    print("punya riwayat?:", hasattr(s, "riwayat"))
    try:
        RiwayatMixin().setor(10)
    except AttributeError as e:
        print("Mixin sendirian: AttributeError:", e)


def main():
    """Alur utama program."""
    percobaan_nama()
    percobaan_kooperatif()
    percobaan_urutan()
    percobaan_mixin()
    percobaan_mixin_salah()


if __name__ == "__main__":
    main()
