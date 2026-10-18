"""Membuktikan alamat pendek tidak ada pada namespace package."""

import perkakas
import alat


def main():
    """Alur utama program."""
    print("perkakas.km_ke_mil ada?", hasattr(perkakas, "km_ke_mil"))
    print("alat.halo ada?", hasattr(alat, "halo"))
    print("alat.sapaan ada?", hasattr(alat, "sapaan"))


if __name__ == "__main__":
    main()
