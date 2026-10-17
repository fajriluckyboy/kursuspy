"""Modul jarak: konversi satuan jarak."""


def km_ke_mil(km):
    """Mengubah kilometer ke mil."""
    return km * 0.621371


def mil_ke_km(mil):
    """Mengubah mil ke kilometer."""
    return mil / 0.621371


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print("10 km =", km_ke_mil(10), "mil")


if __name__ == "__main__":
    main()
