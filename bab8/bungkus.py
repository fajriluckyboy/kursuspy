#!/usr/bin/env python3
"""Pembungkusan: data rekening dan aturannya dikemas dalam satu kelas."""


class Rekening:
    """Rekening bank: data dan aturannya dibungkus bersama."""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self._saldo = saldo

    def setor(self, jumlah):
        """Menambah saldo, jumlah harus positif."""
        if jumlah <= 0:
            raise ValueError(f"jumlah harus positif: {jumlah}")
        self._saldo += jumlah

    def tarik(self, jumlah):
        """Mengurangi saldo, jumlah harus positif dan tidak melebihi saldo."""
        if jumlah <= 0:
            raise ValueError(f"jumlah harus positif: {jumlah}")
        if jumlah > self._saldo:
            raise ValueError(f"saldo kurang: {self._saldo} < {jumlah}")
        self._saldo -= jumlah

    def lihat_saldo(self):
        """Mengembalikan saldo saat ini."""
        return self._saldo


def main():
    """Alur utama program."""
    budi = Rekening("Budi", 100)
    ani = Rekening("Ani", 50)

    budi.setor(25)
    budi.tarik(20)
    print("Saldo Budi:", budi.lihat_saldo())
    print("Saldo Ani :", ani.lihat_saldo())

    for percobaan in (lambda: budi.tarik(500), lambda: budi.setor(-10)):
        try:
            percobaan()
        except ValueError as e:
            print("Ditolak:", e)

    budi._saldo = -999
    print("Dipaksa dari luar:", budi.lihat_saldo())


if __name__ == "__main__":
    main()
