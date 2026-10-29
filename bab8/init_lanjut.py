#!/usr/bin/env python3
"""Parameter __init__ lanjutan: tipe, *args/**kwargs, default list."""


class Produk:
    """Barang yang dijual di toko."""

    def __init__(self, nama, harga, stok=0):
        if not isinstance(nama, str):
            raise TypeError("nama harus berupa teks")
        if not isinstance(harga, (int, float)):
            raise TypeError("harga harus berupa angka")
        if harga < 0:
            raise ValueError("harga tidak boleh negatif")
        self.nama = nama
        self.harga = harga
        self.stok = stok


class Pesanan:
    """Pesanan pelanggan dengan jumlah barang yang bebas."""

    def __init__(self, pelanggan, *barang, **opsi):
        self.pelanggan = pelanggan
        self.barang = list(barang)
        self.opsi = opsi


class KeranjangBuruk:
    """CONTOH JEBAKAN: jangan ditiru."""

    def __init__(self, item=[]):
        self.item = item

    def tambah(self, nama):
        """Tambahkan satu barang ke keranjang."""
        self.item.append(nama)


class KeranjangBaik:
    """Versi benar: tiap keranjang punya list sendiri."""

    def __init__(self, item=None):
        self.item = [] if item is None else list(item)

    def tambah(self, nama):
        """Tambahkan satu barang ke keranjang."""
        self.item.append(nama)


def percobaan_tipe():
    """Percobaan 1: validasi tipe dan nilai."""
    print("== Percobaan 1: tipe ==")
    pensil = Produk("Pensil", 2500, 10)
    print("Berhasil:", vars(pensil))

    try:
        Produk("Buku", "mahal")
    except TypeError as e:
        print("TypeError:", e)

    try:
        Produk("Buku", -100)
    except ValueError as e:
        print("ValueError:", e)


def percobaan_args():
    """Percobaan 2: *args dan **kwargs di __init__."""
    print("== Percobaan 2: args dan kwargs ==")
    p1 = Pesanan(
        "Rani",
        "pensil",
        "penghapus",
        "buku",
        metode="transfer",
        pengiriman="pagi",
    )
    print("p1:", vars(p1))
    p2 = Pesanan("Budi")
    print("p2:", vars(p2))


def percobaan_default():
    """Percobaan 3: jebakan default berupa list."""
    print("== Percobaan 3: default list ==")
    a = KeranjangBuruk()
    b = KeranjangBuruk()
    a.tambah("apel")
    print("Buruk a.item     :", a.item)
    print("Buruk b.item     :", b.item)
    print("Buruk a.item is b.item:", a.item is b.item)

    c = KeranjangBaik()
    d = KeranjangBaik()
    c.tambah("apel")
    print("Baik  c.item     :", c.item)
    print("Baik  d.item     :", d.item)
    print("Baik  c.item is d.item:", c.item is d.item)


def main():
    """Alur utama program."""
    percobaan_tipe()
    percobaan_args()
    percobaan_default()


if __name__ == "__main__":
    main()
