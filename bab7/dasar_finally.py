#!/usr/bin/env python3
"""Latihan try-finally pada keadaan sukses, error, dan return."""


def sukses():
    """try berhasil tanpa error."""
    try:
        print("sukses: isi try")
    finally:
        print("sukses: finally jalan")


def dengan_return():
    """finally tetap jalan walau try sudah return."""
    try:
        print("dengan_return: isi try")
        return "nilai dari try"
    finally:
        print("dengan_return: finally jalan")


def gagal():
    """Error tidak ditangani, finally jalan dulu sebelum error keluar."""
    try:
        print("gagal: isi try")
        print(1 / 0)
    finally:
        print("gagal: finally jalan")


def main():
    """Alur utama program."""
    sukses()
    print(dengan_return())
    gagal()
    print("Tidak tercapai: error dari gagal() belum ditangani")


if __name__ == "__main__":
    main()
