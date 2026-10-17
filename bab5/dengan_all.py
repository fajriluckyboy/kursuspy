"""Modul dengan __all__."""

__all__ = ["publik"]


def publik():
    """Fungsi untuk pengguna."""
    return "publik"


def rahasia():
    """Fungsi yang tidak masuk daftar __all__."""
    return "rahasia"


def main():
    """Alur utama program."""
    print(publik())


if __name__ == "__main__":
    main()
