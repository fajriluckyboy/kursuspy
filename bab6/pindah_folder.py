#!/usr/bin/env python3
"""Latihan berpindah direktori dengan os.chdir() dan os.getcwd()."""

import os


def main():
    """Alur utama program."""
    print("Awal      :", os.getcwd())

    os.chdir("laporan")
    print("Di laporan:", os.getcwd())

    with open("ringkasan.txt", "w", encoding="utf-8") as berkas:
        berkas.write("Ditulis dari dalam folder laporan\n")

    os.chdir("..")
    print("Kembali   :", os.getcwd())
    print("ringkasan di bab6?   ", os.path.exists("ringkasan.txt"))
    print("ringkasan di laporan?", os.path.exists("laporan/ringkasan.txt"))


if __name__ == "__main__":
    main()
