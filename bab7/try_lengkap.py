#!/usr/bin/env python3
"""Latihan bentuk lengkap try-except-else-finally."""


def bagi(a, b):
    """Membagi a dengan b sambil memperlihatkan urutan eksekusi."""
    print(f"--- bagi({a!r}, {b!r}) ---")
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("except: tidak bisa membagi dengan nol")
        return None
    else:
        print("else: pembagian berhasil")
        return hasil
    finally:
        print("finally: selesai")


def main():
    """Alur utama program."""
    print(bagi(10, 2))
    print(bagi(10, 0))
    try:
        print(bagi(10, "dua"))
    except TypeError:
        print("main: TypeError dari bagi() ditangkap di sini")


if __name__ == "__main__":
    main()
