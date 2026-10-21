#!/usr/bin/env python3
"""Latihan dasar assert."""


def rata_rata(daftar):
    """Mengembalikan rata-rata isi daftar yang tidak kosong."""
    assert len(daftar) > 0, "daftar tidak boleh kosong"
    return sum(daftar) / len(daftar)


def main():
    """Alur utama program."""
    assert 1 + 1 == 2
    print("assert tanpa pesan lolos")

    print("Rata-rata:", rata_rata([10, 20, 30]))

    try:
        rata_rata([])
    except AssertionError as e:
        print("Asersi gagal ditangkap:", type(e).__name__, "-", e)

    assert 2 + 2 == 5, "hitungan salah"
    print("Tidak tercapai")


if __name__ == "__main__":
    main()
