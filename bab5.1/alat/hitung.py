"""Modul hitung di dalam namespace package alat."""


def kuadrat(x):
    """Mengembalikan x pangkat dua."""
    return x**2


def main():
    """Uji singkat modul saat dijalankan langsung."""
    print(kuadrat(7))


if __name__ == "__main__":
    main()
