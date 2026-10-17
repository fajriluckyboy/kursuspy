"""Modul berisi kelas bangun datar sederhana."""

PI = 3.14159


class Persegi:
    """Bangun persegi."""

    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi**2

    def keliling(self):
        return 4 * self.sisi


class Lingkaran:
    """Bangun lingkaran."""

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return PI * self.jari_jari**2

    def keliling(self):
        return 2 * PI * self.jari_jari
