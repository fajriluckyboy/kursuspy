#!/usr/bin/env python3
"""super().__init__(): anak memanggil __init__ induk.

Tabungan         : cara standar (super().__init__ di baris pertama)
TabunganTerbalik : super().__init__ di akhir, untuk melihat urutan
TabunganKurang   : super().__init__() tanpa argumen (jebakan)
"""


class Rekening:
    """Kelas induk: pemilik dan saldo, dengan pemeriksaan."""

    def __init__(self, pemilik, saldo=0):
        # Pemeriksaan induk; harus tetap berlaku bagi semua anak
        if saldo < 0:
            raise ValueError("saldo tidak boleh negatif")
        self.pemilik = pemilik
        self.saldo = saldo

    def ringkas(self):
        """Kembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"


class Tabungan(Rekening):
    """Cara standar: parameter induk dulu, lalu milik anak."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5):
        # Serahkan bagian induk (pemilik, saldo) ke induk
        super().__init__(pemilik, saldo)
        # Bagian milik anak sendiri
        self.bunga_persen = bunga_persen

    def ringkas(self):
        """Perluas ringkasan induk dengan info bunga."""
        return f"{super().ringkas()} (bunga {self.bunga_persen}%)"


class TabunganTerbalik(Rekening):
    """Hanya untuk pengamatan urutan: super() ditaruh terakhir."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5):
        self.bunga_persen = bunga_persen
        super().__init__(pemilik, saldo)


class TabunganKurang(Rekening):
    """JEBAKAN: lupa mengirim argumen yang dibutuhkan induk."""

    def __init__(self, pemilik, saldo=0, bunga_persen=5):
        super().__init__()
        self.bunga_persen = bunga_persen


def main():
    """Alur utama program."""
    print("--- Objek lengkap ---")
    t = Tabungan("Fajri", 100, 7)
    print("vars(t)              :", vars(t))
    print("t.ringkas()          :", t.ringkas())

    print("--- Nilai default dan keyword ---")
    t2 = Tabungan("Sari")
    print("vars(t2)             :", vars(t2))
    t3 = Tabungan("Budi", bunga_persen=3)
    print("vars(t3)             :", vars(t3))

    print("--- Pemeriksaan induk tetap berlaku ---")
    try:
        Tabungan("Rusak", -5)
    except ValueError as e:
        print("Gagal dibuat         :", e)

    print("--- Urutan super().__init__() menentukan vars ---")
    tb = TabunganTerbalik("Fajri", 100, 7)
    print("vars(tb)             :", vars(tb))

    print("--- Argumen induk tidak dikirim ---")
    try:
        TabunganKurang("Fajri", 100)
    except TypeError as e:
        print("TypeError:", e)


if __name__ == "__main__":
    main()
