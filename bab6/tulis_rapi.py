#!/usr/bin/env python3
"""Menulis banyak baris dengan writelines() secara rapi."""


def main():
    """Alur utama program."""
    buah = ["Apel", "Jeruk", "Mangga"]
    baris = [f"{nama}\n" for nama in buah]

    berkas = open("buah.txt", "w", encoding="utf-8")
    berkas.writelines(baris)
    berkas.close()
    print("Isi list baris:", baris)


if __name__ == "__main__":
    main()
