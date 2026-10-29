#!/usr/bin/env python3
"""Metode private: underscore tunggal, ganda, dan name mangling.

Publik   : setor, tarik, lihat_saldo, lihat_riwayat
Pembantu : _periksa_jumlah  (konvensi, tidak diblokir)
Private  : __catat          (name mangling)
"""


class Rekening:
    """Rekening dengan bagian dalam yang ditandai private."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        # Awalan _ : data internal, jangan diubah dari luar
        self._saldo = saldo
        self._riwayat = []

    def _periksa_jumlah(self, jumlah):
        """Pembantu: tolak jumlah nol atau negatif."""
        if jumlah <= 0:
            raise ValueError("jumlah harus lebih dari 0")

    def __catat(self, keterangan):
        """Private: simpan satu baris riwayat (name mangling)."""
        self._riwayat.append(f"{keterangan} -> saldo {self._saldo}")

    def setor(self, jumlah):
        """Tambah saldo."""
        self._periksa_jumlah(jumlah)
        self._saldo += jumlah
        # Di dalam kelas, __catat dipanggil dengan nama biasa
        self.__catat(f"setor {jumlah}")

    def tarik(self, jumlah):
        """Kurangi saldo."""
        self._periksa_jumlah(jumlah)
        if jumlah > self._saldo:
            raise ValueError("saldo tidak cukup")
        self._saldo -= jumlah
        self.__catat(f"tarik {jumlah}")

    def lihat_saldo(self):
        """Kembalikan saldo saat ini."""
        return self._saldo

    def lihat_riwayat(self):
        """Kembalikan salinan riwayat agar aslinya aman."""
        return list(self._riwayat)


def main():
    """Alur utama program."""
    rek = Rekening("Fajri")
    rek.setor(100)
    rek.tarik(30)
    print("Saldo   :", rek.lihat_saldo())
    print("Riwayat :", rek.lihat_riwayat())

    print("--- Mencoba menembus dari luar ---")

    # Underscore ganda: nama asli tidak ditemukan dari luar
    try:
        rek.__catat("coba")
    except AttributeError as e:
        print("__catat dari luar:", e)

    # Underscore tunggal: tidak diblokir, hanya konvensi
    try:
        rek._periksa_jumlah(0)
    except ValueError as e:
        print("_periksa_jumlah dari luar tetap jalan:", e)

    # Nama hasil name mangling masih bisa diketik
    rek._Rekening__catat("diketik paksa")
    print("Riwayat terakhir:", rek.lihat_riwayat()[-1])

    # Celah lama: data _saldo tetap bisa ditimpa
    rek._saldo = -999
    print("Saldo setelah ditimpa:", rek.lihat_saldo())

    print("Isi objek:", vars(rek))


if __name__ == "__main__":
    main()
