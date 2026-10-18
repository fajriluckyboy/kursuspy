"""Membuktikan dua folder bernama sama disatukan menjadi satu paket."""

import perusahaan.jarak
import perusahaan.suhu


def main():
    """Alur utama program."""
    print("Kelvin dari 25 C:", perusahaan.suhu.celsius_ke_kelvin(25))
    print("Centimeter dari 3 m:", perusahaan.jarak.meter_ke_cm(3))
    print("__file__:", perusahaan.__file__)
    print("__path__:", perusahaan.__path__)


if __name__ == "__main__":
    main()
