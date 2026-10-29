#!/usr/bin/env python3
"""Mengamati bahwa nilai-nilai biasa adalah objek dari suatu kelas."""


def main():
    """Alur utama program."""
    nilai = [5, "teks", [1, 2], 3.5, True]
    for item in nilai:
        print(f"{item!r:8} -> kelas {type(item).__name__}")

    print("5 instans int?", isinstance(5, int))
    print("5 instans str?", isinstance(5, str))

    a = [1, 2]
    b = [1, 2]
    print("a dan b objek sama?", a is b)
    a.append(3)
    print("a:", a, "| b:", b)


if __name__ == "__main__":
    main()
