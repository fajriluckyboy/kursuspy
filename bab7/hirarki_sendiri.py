#!/usr/bin/env python3
"""Hirarki eksepsi buatan sendiri dengan data tambahan."""


class AplikasiError(Exception):
    """Induk semua error milik aplikasi ini."""


class UmurTidakValidError(AplikasiError):
    """Umur di luar rentang yang sah."""

    def __init__(self, umur):
        super().__init__(f"umur di luar rentang 0-150: {umur}")
        self.umur = umur


class NamaKosongError(AplikasiError):
    """Nama kosong atau hanya berisi spasi."""


def periksa_umur(umur):
    """Mengembalikan umur bila sah, memicu UmurTidakValidError bila tidak."""
    if umur < 0 or umur > 150:
        raise UmurTidakValidError(umur)
    return umur


def periksa_nama(nama):
    """Mengembalikan nama bila tidak kosong, memicu NamaKosongError bila kosong."""
    if nama.strip() == "":
        raise NamaKosongError("nama tidak boleh kosong")
    return nama


def main():
    """Alur utama program."""
    print(
        "UmurTidakValidError anak AplikasiError?",
        issubclass(UmurTidakValidError, AplikasiError),
    )

    try:
        periksa_umur(200)
    except UmurTidakValidError as e:
        print("Spesifik :", e)
        print("Data     :", e.umur)
        print("Args     :", e.args)

    for nama in ("Fajri", "   "):
        try:
            periksa_nama(nama)
        except AplikasiError as e:
            print("Seluruh keluarga tertangkap:", type(e).__name__)
        else:
            print("Nama diterima:", nama)


if __name__ == "__main__":
    main()
