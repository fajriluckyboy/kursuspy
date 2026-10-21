#!/usr/bin/env python3
"""Latihan menangani beberapa tipe eksepsi."""


def ambil(data, kunci, pembagi):
    """Mengambil data[kunci] lalu membaginya dengan pembagi."""
    try:
        nilai = data[kunci]
        hasil = nilai / pembagi
    except KeyError:
        print("KeyError: kunci tidak ada ->", repr(kunci))
    except IndexError:
        print("IndexError: indeks di luar jangkauan ->", kunci)
    except (ZeroDivisionError, TypeError) as e:
        print("Pembagian bermasalah:", type(e).__name__)
    else:
        print("Hasil:", hasil)


def main():
    """Alur utama program."""
    harga = {"apel": 10, "jeruk": 20}
    daftar = [100, 200]

    ambil(harga, "apel", 2)
    ambil(harga, "mangga", 2)
    ambil(daftar, 5, 2)
    ambil(harga, "apel", 0)
    ambil(harga, "apel", "dua")


if __name__ == "__main__":
    main()
