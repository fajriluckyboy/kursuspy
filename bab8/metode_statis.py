#!/usr/bin/env python3
"""Tiga jenis metode: biasa, statis, dan kelas.

Biasa  : ringkas()       -> butuh objek (self)
Statis : saldo_sah()     -> fungsi pembantu, tanpa self dan cls
Kelas  : dari_teks(),
         jumlah_rekening() -> bekerja atas nama kelas (cls)
"""


class Rekening:
    """Rekening bank dengan tiga jenis metode."""

    # Atribut kelas (Bagian A): satu salinan, dipakai bersama
    jumlah = 0

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo
        # Ubah atribut kelas lewat nama kelas
        Rekening.jumlah += 1

    def ringkas(self):
        """Metode biasa: butuh objek, membaca atribut milik objek."""
        return f"{self.pemilik}: Rp{self.saldo}"

    @staticmethod
    def saldo_sah(nilai):
        """Metode statis: tidak butuh objek maupun kelas.

        Hanya memeriksa nilai yang dikirim lewat parameter.
        """
        return isinstance(nilai, (int, float)) and nilai >= 0

    @classmethod
    def dari_teks(cls, teks):
        """Metode kelas: membuat Rekening dari teks 'nama, saldo'."""
        # split(",") memecah teks di tanda koma jadi list (Bab 11)
        pemilik, saldo = teks.split(",")
        # cls(...) sama dengan Rekening(...): membuat objek baru
        return cls(pemilik.strip(), int(saldo))

    @classmethod
    def jumlah_rekening(cls):
        """Metode kelas: membaca atribut kelas lewat cls."""
        return cls.jumlah


def main():
    """Alur utama program."""
    print("--- Metode statis ---")
    print("saldo_sah(100)    :", Rekening.saldo_sah(100))
    print("saldo_sah(-5)     :", Rekening.saldo_sah(-5))
    print("saldo_sah('abc')  :", Rekening.saldo_sah("abc"))

    print("--- Metode kelas: konstruktor alternatif ---")
    r1 = Rekening("Fajri", 100)
    r2 = Rekening.dari_teks("Sari, 250")
    print("r1                :", r1.ringkas())
    print("r2                :", r2.ringkas())
    print("vars(r2)          :", vars(r2))
    print("type(r2)          :", type(r2))

    print("--- Metode kelas: atribut kelas ---")
    print("jumlah_rekening() :", Rekening.jumlah_rekening())

    print("--- Statis dan kelas bisa dipanggil lewat objek ---")
    print("r1.saldo_sah(50)  :", r1.saldo_sah(50))
    print("r1.jumlah_rekening():", r1.jumlah_rekening())

    print("--- Metode biasa tidak bisa lewat kelas tanpa objek ---")
    try:
        Rekening.ringkas()
    except TypeError as e:
        print("TypeError:", e)


if __name__ == "__main__":
    main()
