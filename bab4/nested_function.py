def outer():
    """Fungsi outer dengan fungsi inner sederhana."""
    pesan = "Halo dari outer"

    def inner():
        """Fungsi inner yang mengakses variabel outer."""
        print(pesan)

    inner()


outer()

print("-" * 30)


def buat_pengali(faktor):
    """
    Membuat fungsi pengali dengan faktor tertentu.
    Mengembalikan fungsi inner sebagai closure.
    """

    def kali(angka):
        return angka * faktor

    return kali


kali_dua = buat_pengali(2)
kali_tiga = buat_pengali(3)
kali_sepuluh = buat_pengali(10)

print(kali_dua(5))
print(kali_tiga(5))
print(kali_sepuluh(5))

print("-" * 30)


def outer_counter():
    """Mendemonstrasikan penggunaan nonlocal."""
    counter = 0

    def tambah():
        nonlocal counter
        counter += 1
        print(f"Counter: {counter}")

    tambah()
    tambah()
    tambah()
    print(f"Counter akhir: {counter}")


outer_counter()
