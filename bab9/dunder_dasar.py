#!/usr/bin/env python3
"""Metode khusus (dunder): kelas buatan ikut berpolimorfisme.

Polos    : tanpa metode khusus (pembanding)
Rekening : __repr__, __str__, __eq__, __lt__, __add__
Riwayat  : __len__
"""


class Polos:
    """Kelas tanpa metode khusus."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo


class Rekening:
    """Rekening dengan metode khusus."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def __repr__(self):
        """Teks untuk pengembang, berbentuk kode pembuat objek."""
        return f"Rekening({self.pemilik!r}, {self.saldo!r})"

    def __str__(self):
        """Teks ramah pembaca."""
        return f"{self.pemilik}: Rp{self.saldo}"

    def __eq__(self, lain):
        """Dua rekening sama bila pemilik dan saldonya sama."""
        if not isinstance(lain, Rekening):
            return NotImplemented
        return self.pemilik == lain.pemilik and self.saldo == lain.saldo

    def __lt__(self, lain):
        """Rekening lebih kecil bila saldonya lebih kecil."""
        if not isinstance(lain, Rekening):
            return NotImplemented
        return self.saldo < lain.saldo

    def __add__(self, lain):
        """Rekening + angka menghasilkan Rekening BARU."""
        if not isinstance(lain, (int, float)):
            return NotImplemented
        return Rekening(self.pemilik, self.saldo + lain)


class Riwayat:
    """Daftar catatan transaksi."""

    def __init__(self):
        self._catatan = []

    def tambah(self, teks):
        """Tambahkan satu catatan."""
        self._catatan.append(teks)

    def __len__(self):
        """Jumlah catatan."""
        return len(self._catatan)


def percobaan_polos():
    """Percobaan 1: kelas tanpa metode khusus."""
    print("== Percobaan 1: tanpa metode khusus ==")
    a = Polos("Fajri", 1000)
    b = Polos("Fajri", 1000)
    print("print(a)  :", a)
    print("repr(a)   :", repr(a))
    print("a == b    :", a == b)
    print("a == a    :", a == a)


def percobaan_teks():
    """Percobaan 2: __str__ dan __repr__."""
    print("== Percobaan 2: __str__ dan __repr__ ==")
    r1 = Rekening("Fajri", 1000)
    r2 = Rekening("Sari", 2000)
    print("print(r1)   :", r1)
    print("str(r1)     :", str(r1))
    print("repr(r1)    :", repr(r1))
    print("f-string    :", f"{r1}")
    print("f-string !r :", f"{r1!r}")
    print("dalam list  :", [r1, r2])


def percobaan_sama():
    """Percobaan 3: __eq__."""
    print("== Percobaan 3: __eq__ ==")
    r1 = Rekening("Fajri", 1000)
    r2 = Rekening("Fajri", 1000)
    r3 = Rekening("Sari", 1000)
    print("r1 == r2        :", r1 == r2)
    print("r1 is r2        :", r1 is r2)
    print("r1 == r3        :", r1 == r3)
    print("r1 != r2        :", r1 != r2)
    print("r1 == 'Fajri'   :", r1 == "Fajri")
    print("r1 in [r3, r2]  :", r1 in [r3, r2])


def percobaan_urut():
    """Percobaan 4: __lt__."""
    print("== Percobaan 4: __lt__ ==")
    daftar = [
        Rekening("Fajri", 3000),
        Rekening("Sari", 1000),
        Rekening("Budi", 2000),
    ]
    print("sorted      :", sorted(daftar))
    print("d0 < d1     :", daftar[0] < daftar[1])
    print("d0 > d1     :", daftar[0] > daftar[1])


def percobaan_tambah_len():
    """Percobaan 5: __add__ dan __len__."""
    print("== Percobaan 5: __add__ dan __len__ ==")
    r = Rekening("Fajri", 1000)
    baru = r + 500
    print("r.saldo     :", r.saldo)
    print("baru.saldo  :", baru.saldo)
    print("r is baru   :", r is baru)
    try:
        r + "x"
    except TypeError as e:
        print("r + 'x'     : TypeError:", e)
    try:
        len(r)
    except TypeError as e:
        print("len(r)      : TypeError:", e)
    h = Riwayat()
    print("len kosong  :", len(h), "| bool:", bool(h))
    h.tambah("setor 50")
    print("len isi 1   :", len(h), "| bool:", bool(h))


def percobaan_hash():
    """Percobaan 6: akibat menulis __eq__ terhadap hash."""
    print("== Percobaan 6: hash ==")
    print("tipe hash(Polos)  :", type(hash(Polos("Fajri"))).__name__)
    print("Rekening.__hash__ :", Rekening.__hash__)
    r = Rekening("Fajri", 1000)
    try:
        {r}
    except TypeError as e:
        print("set       : TypeError:", e)
    try:
        {r: "kunci"}
    except TypeError as e:
        print("kunci dict: TypeError:", e)


def main():
    """Alur utama program."""
    percobaan_polos()
    percobaan_teks()
    percobaan_sama()
    percobaan_urut()
    percobaan_tambah_len()
    percobaan_hash()


if __name__ == "__main__":
    main()
