"""Modul jarak, bagian dari paket perusahaan di lokasi B."""


def meter_ke_cm(m):
    """Mengubah meter ke sentimeter."""
    return m * 100


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print(meter_ke_cm(2))


if __name__ == "__main__":
    main()
