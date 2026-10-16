def tampil_info(**kwargs):
    """Menampilkan informasi dari kwargs."""
    print(f"Tipe: {type(kwargs)}")
    for kunci, nilai in kwargs.items():
        print(f"{kunci}: {nilai}")


tampil_info(nama="Fajri", umur=20, kota="Makassar")
print("-" * 30)
tampil_info(bahasa="Python", versi="3.13", platform="Termux")

print("-" * 30)


def lengkap(judul, *args, **kwargs):
    """Fungsi dengan semua jenis parameter."""
    print(f"Judul  : {judul}")
    print(f"Args   : {args}")
    print(f"Kwargs : {kwargs}")


lengkap("Data Saya", 1, 2, 3, nama="Fajri", kota="Makassar")
