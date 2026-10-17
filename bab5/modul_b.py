"""Modul B: mengimpor modul A (dan sebaliknya)."""

from modul_a import salam_a


def salam_b():
    """Mengembalikan salam dari modul B."""
    return "Halo dari B"


def main():
    """Alur utama program."""
    print(salam_b())
    print(salam_a())


if __name__ == "__main__":
    main()
