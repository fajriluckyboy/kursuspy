"""Modul sapaan di dalam namespace package alat."""


def halo(nama):
    """Mengembalikan sapaan untuk nama yang diberikan."""
    return f"Halo, {nama}!"


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print(halo("Fajri"))


if __name__ == "__main__":
    main()
