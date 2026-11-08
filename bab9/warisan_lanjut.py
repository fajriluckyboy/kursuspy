#!/usr/bin/env python3
"""Pewarisan lanjutan: pewarisan keliru, komposisi, atribut induk.

Percobaan 1: NasabahKeliru mewarisi Rekening (uji is-a gagal).
Percobaan 2: RekeningBaik memegang Nasabah (komposisi, has-a).
Percobaan 3: atribut kelas induk dilihat dari kelas anak.
"""


class Rekening:
    """Kelas induk: rekening bank umum."""

    # Atribut kelas (Bab 8 Sub-materi 9)
    BANK = "Bank Kursus"

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
    """Kelas anak yang sah: Tabungan adalah sebuah Rekening."""

    pass


class NasabahKeliru(Rekening):
    """CONTOH KELIRU: nasabah bukan sebuah rekening. Jangan ditiru."""

    pass


class Nasabah:
    """Data orang: nama dan kota. Bukan rekening."""

    def __init__(self, nama, kota):
        self.nama = nama
        self.kota = kota


class RekeningBaik:
    """Komposisi: rekening PUNYA seorang nasabah."""

    def __init__(self, nasabah, saldo=0):
        # Atribut berisi objek lain: inilah komposisi
        self.nasabah = nasabah
        self.saldo = saldo

    def ringkas(self):
        """Kembalikan teks ringkasan, data nama lewat objek nasabah."""
        return f"{self.nasabah.nama} ({self.nasabah.kota}): " f"Rp{self.saldo}"


def percobaan_keliru():
    """Percobaan 1: pewarisan yang gagal uji is-a."""
    print("== Percobaan 1: pewarisan keliru ==")
    n = NasabahKeliru("Fajri")
    # Nasabah yang bisa disetori uang: tidak masuk akal
    n.setor(100)
    print("n.ringkas()              :", n.ringkas())
    print("isinstance(n, Rekening)  :", isinstance(n, Rekening))


def percobaan_komposisi():
    """Percobaan 2: komposisi, rekening memegang nasabah."""
    print("== Percobaan 2: komposisi ==")
    sari = Nasabah("Sari", "Makassar")
    rek = RekeningBaik(sari, 250)
    print("rek.ringkas()            :", rek.ringkas())
    print("isinstance(rek, Rekening):", isinstance(rek, Rekening))
    print("isinstance(rek.nasabah, Nasabah):", isinstance(rek.nasabah, Nasabah))


def percobaan_atribut_induk():
    """Percobaan 3: atribut kelas induk dilihat dari anak."""
    print("== Percobaan 3: atribut kelas induk ==")
    t = Tabungan("Fajri", 100)

    print("'BANK' in vars(Tabungan) :", "BANK" in vars(Tabungan))
    print("Tabungan.BANK            :", Tabungan.BANK)

    print("--- Ubah di induk ---")
    Rekening.BANK = "Bank Baru"
    print("Tabungan.BANK            :", Tabungan.BANK)
    print("t.BANK                   :", t.BANK)

    print("--- Tulis lewat kelas anak ---")
    Tabungan.BANK = "Bank Tabungan"
    print("Tabungan.BANK            :", Tabungan.BANK)
    print("Rekening.BANK            :", Rekening.BANK)
    print("t.BANK                   :", t.BANK)
    print("'BANK' in vars(Tabungan) :", "BANK" in vars(Tabungan))


def main():
    """Alur utama program."""
    percobaan_keliru()
    percobaan_komposisi()
    percobaan_atribut_induk()


if __name__ == "__main__":
    main()
