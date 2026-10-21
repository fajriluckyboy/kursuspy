#!/usr/bin/env python3
"""Melihat silsilah beberapa kelas eksepsi."""


def tampilkan(kelas):
    """Mencetak silsilah sebuah kelas dari dirinya sampai akar."""
    nama = [k.__name__ for k in kelas.__mro__]
    print(" -> ".join(nama))


def main():
    """Alur utama program."""
    tampilkan(ZeroDivisionError)
    tampilkan(FileExistsError)
    tampilkan(ModuleNotFoundError)
    tampilkan(KeyError)
    print(issubclass(FileExistsError, OSError))
    print(issubclass(FileExistsError, ValueError))


if __name__ == "__main__":
    main()
