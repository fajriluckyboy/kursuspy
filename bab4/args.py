def jumlahkan(*args):
    """Menjumlahkan berapapun angka."""
    print(f"Argumen diterima: {args}")
    print(f"Tipe: {type(args)}")
    total = 0
    for angka in args:
        total += angka
    return total


print(jumlahkan(1, 2))
print(jumlahkan(1, 2, 3, 4, 5))
print(jumlahkan(10, 20, 30, 40, 50, 60))

print("-" * 30)


def info(judul, *args):
    """Menampilkan data dengan judul."""
    print(f"--- {judul} ---")
    for item in args:
        print(item)


info("Biodata", "Fajri", 20, "Makassar")
info("Bahasa", "Python", "JavaScript", "Rust")
