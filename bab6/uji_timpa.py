#!/usr/bin/env python3
"""Membuktikan mode w menimpa isi lama file."""


def main():
    """Alur utama program."""
    berkas = open("data_write.txt", "w", encoding="utf-8")
    berkas.write("Isi baru saja\n")
    berkas.close()


if __name__ == "__main__":
    main()
