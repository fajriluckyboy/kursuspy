"""Menampilkan lokasi pencarian impor milik Python."""

import sys


def main():
    """Alur utama program."""
    for nomor, lokasi in enumerate(sys.path):
        print(nomor, lokasi)


if __name__ == "__main__":
    main()
