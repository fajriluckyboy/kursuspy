#!/usr/bin/env python3
"""Membuktikan with menutup file walau terjadi error."""


def tulis_dengan_with():
    """Menulis lewat with, lalu memicu error di dalam blok."""
    with open("hasil_with.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Data aman karena with\n")
        print(1 / 0)
        berkas.write("Baris ini tak pernah tertulis\n")


def tulis_manual():
    """Menulis lewat open() manual, lalu memicu error sebelum close()."""
    berkas = open("hasil_manual.txt", "w", encoding="utf-8")
    berkas.write("Data rawan karena manual\n")
    print(1 / 0)
    berkas.close()


def main():
    """Alur utama program."""
    try:
        tulis_dengan_with()
    except ZeroDivisionError:
        print("Error terjadi pada versi with")

    try:
        tulis_manual()
    except ZeroDivisionError:
        print("Error terjadi pada versi manual")

    with open("hasil_with.txt", "r", encoding="utf-8") as berkas:
        print("Isi hasil_with.txt  :", repr(berkas.read()))


if __name__ == "__main__":
    main()
