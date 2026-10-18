"""Modul suhu: konversi satuan suhu."""


def celsius_ke_fahrenheit(c):
    """Mengubah suhu Celsius ke Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_ke_celsius(f):
    """Mengubah suhu Fahrenheit ke Celsius."""
    return (f - 32) * 5 / 9


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print("100 C =", celsius_ke_fahrenheit(100), "F")


if __name__ == "__main__":
    main()
