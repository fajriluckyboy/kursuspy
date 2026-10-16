print("=== Satu Pernyataan ===")
exec("x = 10")
print(x)

print("=== Banyak Baris ===")
kode = """
a = 5
b = 3
print(a + b)
print(a * b)
"""
exec(kode)

print("=== Membuat Fungsi ===")
kode_fungsi = """
def sapa(nama):
    print(f"Halo, {nama}!")
"""
exec(kode_fungsi)
sapa("Fajri")

print("=== Nilai Balik exec ===")
hasil = exec("y = 99")
print(hasil)
print(y)
