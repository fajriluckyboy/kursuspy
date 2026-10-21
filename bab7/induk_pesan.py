#!/usr/bin/env python3
"""Menangkap induk LookupError dan membaca isi objek error."""


def cari(data, kunci):
    """Mengambil data[kunci], melaporkan bila gagal."""
    try:
        return data[kunci]
    except LookupError as e:
        print("Jenis    :", type(e).__name__)
        print("Pesan    :", str(e))
        print("Args     :", e.args)
        print("Anak dari LookupError?", isinstance(e, LookupError))
        return None


def main():
    """Alur utama program."""
    print(cari({"a": 1}, "b"))
    print(cari([10, 20], 9))
    print(cari({"a": 1}, "a"))


if __name__ == "__main__":
    main()
