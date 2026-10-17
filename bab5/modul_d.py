"""Modul D: memakai modul salam dan modul C."""

from salam import salam_b
import modul_c


def main():
    """Alur utama program."""
    print("Modul D memanggil:", salam_b())
    modul_c.main()


if __name__ == "__main__":
    main()
