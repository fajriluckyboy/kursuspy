#!/usr/bin/env python3
"""Jebakan: __init__ anak menutupi __init__ induk.

Induk : Rekening       (__init__ mengisi pemilik dan saldo)
Anak  : TabunganRusak  (__init__ sendiri, tidak mengurus induk)
"""


class Rekening:
    """Kelas induk: rekening bank umum."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def ringkas(self):
        """Kembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"


class TabunganRusak(Rekening):
    """CONTOH JEBAKAN: jangan ditiru.

    __init__ di sini menutupi __init__ milik Rekening.
    """

    def __init__(self, bunga_persen):
        # Hanya mengisi bunga_persen; pemilik dan saldo terlupakan
        self.bunga_persen = bunga_persen


def main():
    """Alur utama program."""
    print("--- Objek dibuat dengan __init__ anak ---")
    t = TabunganRusak(5)
    print("vars(t)                     :", vars(t))
    print("hasattr(t, 'bunga_persen')  :", hasattr(t, "bunga_persen"))
    print("hasattr(t, 'pemilik')       :", hasattr(t, "pemilik"))
    print("hasattr(t, 'saldo')         :", hasattr(t, "saldo"))

    print("--- Metode induk tetap ada, tetapi datanya tidak ---")
    print("hasattr(t, 'ringkas')       :", hasattr(t, "ringkas"))
    try:
        print(t.ringkas())
    except AttributeError as e:
        print("AttributeError:", e)

    print("--- __init__ induk tidak rusak, hanya tertutup ---")
    print("'__init__' in vars(Rekening):", "__init__" in vars(Rekening))
    print("'__init__' in vars(TabunganRusak):", "__init__" in vars(TabunganRusak))
    r = Rekening("Sari", 100)
    print("r.ringkas()                 :", r.ringkas())

    print("--- Argumen untuk induk ditolak ---")
    try:
        TabunganRusak("Fajri", 100)
    except TypeError as e:
        print("TypeError:", e)


if __name__ == "__main__":
    main()
