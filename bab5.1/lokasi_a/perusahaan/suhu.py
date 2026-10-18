"""Modul suhu, bagian dari paket perusahaan di lokasi A."""


def celsius_ke_kelvin(c):
    """Mengubah suhu Celsius ke Kelvin."""
    return c + 273.15


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print(celsius_ke_kelvin(0))


if __name__ == "__main__":
    main()
