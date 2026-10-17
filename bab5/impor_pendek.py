"""Latihan memakai alamat pendek dari paket perkakas."""

import perkakas
from perkakas import celsius_ke_fahrenheit, km_ke_mil


def main():
    """Alur utama program."""
    print("Alamat pendek 1:", celsius_ke_fahrenheit(37))
    print("Alamat pendek 2:", km_ke_mil(42))
    print("Alamat panjang:", perkakas.suhu.fahrenheit_ke_celsius(212))
    print("Daftar API publik:", perkakas.__all__)
    print("Docstring paket:", perkakas.__doc__)


if __name__ == "__main__":
    main()
