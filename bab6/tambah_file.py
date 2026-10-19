#!/usr/bin/env python3
"""Membuktikan mode a menambah teks tanpa menghapus isi lama."""


def main():
    """Alur utama program."""
    berkas = open("riwayat.txt", "a", encoding="utf-8")
    berkas.write("Satu catatan baru\n")
    berkas.close()


if __name__ == "__main__":
    main()
