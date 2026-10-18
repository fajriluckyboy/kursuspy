"""Modul milik paket_uji di lokasi C (namespace)."""


def asal():
    """Mengembalikan asal modul."""
    return "lokasi C"


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print(asal())


if __name__ == "__main__":
    main()
