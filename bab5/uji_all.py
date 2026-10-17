"""Membuktikan pengaruh __all__ pada wildcard."""

import dengan_all
import tanpa_all


def main():
    """Alur utama program."""
    ruang_a = {}
    ruang_b = {}
    exec("from tanpa_all import *", ruang_a)
    exec("from dengan_all import *", ruang_b)
    print("tanpa_all membawa publik   :", "publik" in ruang_a)
    print("tanpa_all membawa _internal:", "_internal" in ruang_a)
    print("dengan_all membawa publik  :", "publik" in ruang_b)
    print("dengan_all membawa rahasia :", "rahasia" in ruang_b)


if __name__ == "__main__":
    main()
