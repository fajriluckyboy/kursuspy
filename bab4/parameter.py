def tambah(a, b):
    """Menjumlahkan dua bilangan."""
    return a + b


print(tambah(3, 4))
print(tambah(10, 20))
print(tambah(100, 200))


def luas_persegi(sisi):
    """Menghitung luas persegi."""
    return sisi * sisi


print(luas_persegi(5))
print(luas_persegi(10))
print(luas_persegi(3))


def biodata(nama, umur, kota):
    """Menampilkan biodata."""
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Kota: {kota}")


biodata("Fajri", 20, "Makassar")
biodata("Budi", 25, "Jakarta")
