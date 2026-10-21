#!/usr/bin/env python3
"""Latihan membuat kelas eksepsi buatan sendiri."""


class UmurTidakValidError(Exception):
    """Umur di luar rentang yang sah."""


def periksa_umur(umur):
    """Mengembalikan umur bila sah, memicu UmurTidakValidError bila tidak."""
    if umur < 0 or umur > 150:
        raise UmurTidakValidError(f"umur di luar rentang 0-150: {umur}")
    return umur


def main():
    """Alur utama program."""
    print("Induk langsung:", UmurTidakValidError.__mro__[1].__name__)
    print("Turunan Exception?", issubclass(UmurTidakValidError, Exception))
    print("Turunan ValueError?", issubclass(UmurTidakValidError, ValueError))

    try:
        periksa_umur(200)
    except UmurTidakValidError as e:
        print("Ditangkap:", type(e).__name__, "-", e)

    try:
        int("abc")
    except UmurTidakValidError:
        print("Tidak tercapai")
    except ValueError:
        print("int('abc') bukan milik kita: ValueError biasa")

    print(periksa_umur(-1))


if __name__ == "__main__":
    main()
