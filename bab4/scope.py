pesan = "Halo dari global"
nilai = 100
counter = 0


def tampilkan():
    """Membaca variabel global dari dalam fungsi."""
    print(pesan)


def ubah_nilai():
    """Variabel lokal tidak mempengaruhi global."""
    nilai = 999
    print(f"Di dalam fungsi: {nilai}")


def tambah_counter():
    """Mengubah variabel global dengan kata kunci global."""
    global counter
    counter += 1
    print(f"Counter sekarang: {counter}")


tampilkan()
ubah_nilai()
print(f"Di luar fungsi: {nilai}")

print("-" * 30)

tambah_counter()
tambah_counter()
tambah_counter()
print(f"Counter akhir: {counter}")
