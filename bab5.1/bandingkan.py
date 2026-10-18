"""Membandingkan regular package dan namespace package."""

import alat
import perkakas


def main():
    """Alur utama program."""
    print("== perkakas (regular package) ==")
    print("__file__:", perkakas.__file__)
    print("__path__:", perkakas.__path__)
    print("__doc__ :", perkakas.__doc__)
    print()
    print("== alat (namespace package) ==")
    print("__file__:", alat.__file__)
    print("__path__:", alat.__path__)
    print("__doc__ :", alat.__doc__)


if __name__ == "__main__":
    main()
