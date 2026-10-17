"""Modul A: mengimpor modul B (dan sebaliknya)."""

from modul_b import salam_b


def salam_a():
    """Mengembalikan salam dari modul A."""
    return "Halo dari A"


def main():
    """Alur utama program."""
    print(salam_a())
    print(salam_b())


if __name__ == "__main__":
    main()
