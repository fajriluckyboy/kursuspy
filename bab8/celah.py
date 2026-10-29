#!/usr/bin/env python3
"""Membuktikan dua celah pada gaya prosedural."""


def buat_rekening(pemilik, saldo):
    """Mengembalikan dict yang mewakili sebuah rekening."""
    return {"pemilik": pemilik, "saldo": saldo}


def setor(rekening, jumlah):
    """Menambah saldo rekening."""
    rekening["saldo"] += jumlah


def main():
    """Alur utama program."""
    budi = buat_rekening("Budi", 100)

    budi["saldo"] = -999
    print("Celah 1, saldo dipaksa dari luar:", budi)

    rusak = {"nama": "Bukan rekening"}
    try:
        setor(rusak, 10)
    except KeyError as e:
        print("Celah 2, dict salah diterima fungsi:", type(e).__name__, e)


if __name__ == "__main__":
    main()
