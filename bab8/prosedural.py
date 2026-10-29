#!/usr/bin/env python3
"""Rekening bank bergaya prosedural: data dan fungsi terpisah."""


def buat_rekening(pemilik, saldo):
    """Mengembalikan dict yang mewakili sebuah rekening."""
    return {"pemilik": pemilik, "saldo": saldo}


def setor(rekening, jumlah):
    """Menambah saldo rekening."""
    rekening["saldo"] += jumlah


def tarik(rekening, jumlah):
    """Mengurangi saldo rekening, memicu ValueError bila saldo kurang."""
    if jumlah > rekening["saldo"]:
        raise ValueError(f"saldo kurang: {rekening['saldo']} < {jumlah}")
    rekening["saldo"] -= jumlah


def main():
    """Alur utama program."""
    budi = buat_rekening("Budi", 100)
    ani = buat_rekening("Ani", 50)

    setor(budi, 25)
    tarik(ani, 20)
    print(budi)
    print(ani)

    try:
        tarik(ani, 500)
    except ValueError as e:
        print("Ditolak:", e)


if __name__ == "__main__":
    main()
