#!/usr/bin/env python3
"""Mengamati tiga prinsip OOP pada objek bawaan Python."""


def amati_pembungkusan():
    """Pembungkusan: objek list membawa data sekaligus metodenya."""
    print("== Pembungkusan ==")
    daftar = [3, 1, 2]
    daftar.sort()
    print("list setelah sort :", daftar)
    print("punya sort?       :", hasattr(daftar, "sort"))
    print("punya append?     :", hasattr(daftar, "append"))
    print("punya upper?      :", hasattr(daftar, "upper"))


def amati_pewarisan():
    """Pewarisan: bool mengambil sifat dari int."""
    print("== Pewarisan ==")
    print("bool turunan int? :", issubclass(bool, int))
    print("True + True       :", True + True)
    nama = [k.__name__ for k in bool.__mro__]
    print("silsilah bool     :", " -> ".join(nama))


def amati_polimorfisme():
    """Polimorfisme: perintah yang sama bekerja pada banyak jenis objek."""
    print("== Polimorfisme ==")
    for item in ("abc", [1, 2, 3], {"a": 1}, (1, 2)):
        print(f"{type(item).__name__:6} len = {len(item)}")
    print("1 + 2         =", 1 + 2)
    print("'a' + 'b'     =", "a" + "b")
    print("[1] + [2]     =", [1] + [2])


def main():
    """Alur utama program."""
    amati_pembungkusan()
    amati_pewarisan()
    amati_polimorfisme()


if __name__ == "__main__":
    main()
