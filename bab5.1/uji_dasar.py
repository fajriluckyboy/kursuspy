"""Membuktikan folder tanpa __init__.py tetap bisa diimpor."""

import alat.hitung
from alat import sapaan


def main():
    """Alur utama program."""
    print(sapaan.halo("Fajri"))
    print("Kuadrat 9:", alat.hitung.kuadrat(9))


if __name__ == "__main__":
    main()
