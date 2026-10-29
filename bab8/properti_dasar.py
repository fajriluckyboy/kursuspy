#!/usr/bin/env python3
"""Properti: getter, setter dengan validasi, dan properti hanya-baca.

Properti saldo menutup celah lama: saldo tidak lagi bisa
diisi nilai negatif atau bertipe salah dari luar kelas.
"""


class Rekening:
    """Rekening yang saldonya dijaga oleh properti."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        # Baris ini TIDAK menulis langsung ke atribut.
        # Karena saldo adalah properti, Python menjalankan setter
        # di bawah, sehingga saldo awal ikut divalidasi.
        self.saldo = saldo

    @property
    def saldo(self):
        """Getter: dijalankan saat saldo DIBACA (rek.saldo)."""
        return self._saldo

    @saldo.setter
    def saldo(self, nilai):
        """Setter: dijalankan saat saldo DIISI (rek.saldo = x)."""
        # Periksa TIPE dulu, baru NILAI (Sub-materi 6)
        if not isinstance(nilai, (int, float)):
            raise TypeError("saldo harus berupa angka")
        if nilai < 0:
            raise ValueError("saldo tidak boleh negatif")
        # Penyimpanan asli memakai nama berbeda (_saldo).
        # Jika ditulis self.saldo = nilai, setter memanggil dirinya
        # sendiri tanpa henti.
        self._saldo = nilai

    @property
    def kosong(self):
        """Properti hanya-baca: tidak punya setter."""
        return self._saldo == 0

    def setor(self, jumlah):
        """Tambah saldo; penjagaan nilai ditangani setter."""
        # self.saldo += jumlah  berarti  self.saldo = self.saldo + jumlah
        # sehingga getter dan setter sama-sama ikut bekerja.
        self.saldo += jumlah


def main():
    """Alur utama program."""
    rek = Rekening("Fajri", 100)
    print("Saldo awal    :", rek.saldo)

    rek.saldo = 250
    print("Setelah diisi :", rek.saldo)

    rek.setor(50)
    print("Setelah setor :", rek.saldo)

    # Celah lama ditutup: nilai buruk ditolak oleh setter
    try:
        rek.saldo = -999
    except ValueError as e:
        print("Ditolak (nilai):", e)

    try:
        rek.saldo = "banyak"
    except TypeError as e:
        print("Ditolak (tipe) :", e)

    # Objek yang lahir dengan saldo buruk pun gagal dibuat
    try:
        Rekening("Rusak", -5)
    except ValueError as e:
        print("Gagal dibuat   :", e)

    print("Kosong?       :", rek.kosong)

    # Properti hanya-baca tidak bisa diisi
    try:
        rek.kosong = True
    except AttributeError as e:
        print("Hanya-baca    :", e)

    # Perhatikan atribut yang benar-benar tersimpan di objek
    print("Isi objek     :", vars(rek))


if __name__ == "__main__":
    main()
