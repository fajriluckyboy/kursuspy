#!/usr/bin/env python3
"""Latihan membuat direktori dengan os.mkdir() dan os.makedirs()."""

import os


def main():
    """Alur utama program."""
    print("laporan ada sebelum?", os.path.isdir("laporan"))
    if not os.path.isdir("laporan"):
        os.mkdir("laporan")
        print("laporan dibuat")
    else:
        print("laporan sudah ada, dilewati")

    os.makedirs("arsip/2026/oktober", exist_ok=True)
    print("arsip/2026/oktober ada?", os.path.isdir("arsip/2026/oktober"))
    print("arsip/2026 ada?", os.path.isdir("arsip/2026"))


if __name__ == "__main__":
    main()
