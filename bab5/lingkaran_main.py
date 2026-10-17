"""Modul hitung lingkaran dengan pola main()."""

PI = 3.14159


def luas(r):
    """Mengembalikan luas lingkaran dengan jari-jari r."""
    return PI * r**2


def main():
    """Alur utama program."""
    r = float(input("Jari-jari: "))
    print("Luas:", luas(r))


if __name__ == "__main__":
    main()
