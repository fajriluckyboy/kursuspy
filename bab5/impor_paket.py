"""Latihan tiga cara mengimpor modul dari dalam paket."""

import perkakas.suhu
from perkakas import jarak
from perkakas.suhu import fahrenheit_ke_celsius as f_ke_c


def main():
    """Alur utama program."""
    print("Cara 1:", perkakas.suhu.celsius_ke_fahrenheit(100))
    print("Cara 2:", jarak.km_ke_mil(10))
    print("Cara 3:", f_ke_c(212))


if __name__ == "__main__":
    main()
