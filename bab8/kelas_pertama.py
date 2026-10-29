#!/usr/bin/env python3
"""Kelas buatan pertama: cetakan kosong dan objek-objeknya."""


class Rekening:
    """Cetakan rekening bank (masih kosong)."""


def main():
    """Alur utama program."""
    print("Rekening itu apa?", type(Rekening).__name__)

    budi = Rekening()
    ani = Rekening()
    print("budi bertipe  :", type(budi).__name__)
    print("budi instans Rekening?", isinstance(budi, Rekening))
    print("budi dan ani objek sama?", budi is ani)

    budi.pemilik = "Budi"
    budi.saldo = 100
    print("Budi:", budi.pemilik, budi.saldo)

    try:
        print(ani.pemilik)
    except AttributeError as e:
        print("Ani belum punya data:", e)


if __name__ == "__main__":
    main()
