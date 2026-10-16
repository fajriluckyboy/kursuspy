def sapa(nama, salam="Halo"):
    """Menyapa dengan salam default atau kustom."""
    print(f"{salam}, {nama}!")


sapa("Fajri")
sapa("Fajri", "Selamat pagi")
sapa("Budi", "Hai")

print("-" * 30)


def biodata(nama, umur, kota="Tidak diketahui", pekerjaan="Pelajar"):
    """Menampilkan biodata dengan nilai default."""
    print(f"Nama     : {nama}")
    print(f"Umur     : {umur}")
    print(f"Kota     : {kota}")
    print(f"Pekerjaan: {pekerjaan}")


biodata("Fajri", 20)
print("-" * 30)
biodata("Budi", 25, "Jakarta")
print("-" * 30)
biodata("Andi", 30, pekerjaan="Programmer")
