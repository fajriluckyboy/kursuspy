"""Membuktikan regular package menang atas namespace package."""

import paket_uji


def main():
    """Alur utama program."""
    print("__file__:", paket_uji.__file__)
    print("__path__:", paket_uji.__path__)
    print("__doc__ :", paket_uji.__doc__)


if __name__ == "__main__":
    main()
