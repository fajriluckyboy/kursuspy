"""Modul tanpa __all__."""


def publik():
    """Fungsi untuk pengguna."""
    return "publik"


def _internal():
    """Fungsi internal, diawali garis bawah."""
    return "internal"


def main():
    """Alur utama program."""
    print(publik())


if __name__ == "__main__":
    main()
