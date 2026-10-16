def sapa(nama):
    """Menyapa pengguna berdasarkan nama."""
    print(f"Halo, {nama}!")
    print("Selamat datang!")


def garis_pemisah():
    """Mencetak garis pemisah."""
    print("-" * 30)


def luas_persegi(sisi):
    """Menghitung luas persegi."""
    return sisi * sisi


def keliling_lingkaran(jari_jari):
    """Menghitung keliling lingkaran."""
    PI = 3.14159
    return 2 * PI * jari_jari


garis_pemisah()
sapa("Fajri")
garis_pemisah()
print(luas_persegi(5))
print(keliling_lingkaran(7))
garis_pemisah()
