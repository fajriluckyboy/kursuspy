def garis():
    """Mencetak garis pemisah."""
    print("-" * 20)


def sapa(nama):
    """Menyapa pengguna."""
    print(f"Halo, {nama}!")


def kuadrat(n):
    """Menghitung kuadrat bilangan."""
    return n * n


def tambah(a, b):
    """Menjumlahkan dua bilangan."""
    return a + b


def sambut(nama):
    """Menyambut pengguna dengan garis."""
    garis()
    sapa(nama)
    garis()


sambut("Fajri")

hasil = kuadrat(5)
print(hasil)
print(kuadrat(10))

print(tambah(3, 4) * 2)
print(tambah(tambah(1, 2), tambah(3, 4)))
