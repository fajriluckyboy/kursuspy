#!/usr/bin/env python3
"""Membuktikan os.rmdir() menolak folder yang tidak kosong."""

import os


def main():
    """Alur utama program."""
    print("laporan ada?", os.path.isdir("laporan"))
    os.rmdir("laporan")
    print("Baris ini tidak tercapai")


if __name__ == "__main__":
    main()
