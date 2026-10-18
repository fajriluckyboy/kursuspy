"""Membuktikan modul di namespace package yang kalah tidak bisa diimpor."""

import paket_uji.modul_c


def main():
    """Alur utama program."""
    print("modul_c ditemukan:", paket_uji.modul_c.asal())


if __name__ == "__main__":
    main()
