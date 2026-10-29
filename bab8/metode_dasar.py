#!/usr/bin/env python3
"""Metode dasar: pengubah, pembaca, dan rantai pemanggilan.

Kelas Rekening menyimpan saldo dan menyediakan tindakan
setor dan tarik. Aturan saldo dijaga di dalam metode.
"""


class Rekening:
    """Rekening sederhana milik satu pemilik."""

    def __init__(self, pemilik, saldo=0):
        # Atribut disimpan di objek lewat self
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        """Tambah saldo. Menolak jumlah nol atau negatif."""
        # Validasi di dalam metode: fail fast (Sub-materi 6)
        if jumlah <= 0:
            raise ValueError("jumlah setor harus lebih dari 0")
        self.saldo += jumlah
        # Mengembalikan objek sendiri agar bisa dirantai
        return self

    def tarik(self, jumlah):
        """Kurangi saldo. Menolak jumlah tidak sah atau saldo kurang."""
        if jumlah <= 0:
            raise ValueError("jumlah tarik harus lebih dari 0")
        if jumlah > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= jumlah
        return self

    def ringkas(self):
        """Kembalikan teks ringkasan. Hanya membaca, tidak mengubah."""
        return f"{self.pemilik}: Rp{self.saldo}"


def main():
    """Alur utama program."""
    rek = Rekening("Fajri", 100)
    print(rek.ringkas())

    # Satu pemanggilan per baris
    rek.setor(50)
    print("Setelah setor 50 :", rek.ringkas())

    # Rantai pemanggilan: setor lalu tarik dalam satu ekspresi
    rek.setor(20).tarik(70)
    print("Setelah rantai   :", rek.ringkas())

    # Aturan di dalam metode menolak tindakan tidak sah
    try:
        rek.tarik(9999)
    except ValueError as e:
        print("Ditolak:", e)


if __name__ == "__main__":
    main()
