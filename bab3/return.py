def tambah(a, b):
    return a + b


hasil = tambah(3, 4)
print(hasil)


def cek_umur(umur):
    if umur < 0:
        return "Umur tidak valid"
    if umur < 17:
        return "Belum cukup umur"
    return "Cukup umur"


print(cek_umur(-1))
print(cek_umur(15))
print(cek_umur(20))


def sapa(nama):
    if nama == "":
        return
    print(f"Halo, {nama}!")


sapa("")
sapa("Fajri")
