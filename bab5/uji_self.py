from bangun import Persegi

a = Persegi(3)
b = Persegi(8)

print("Sisi a:", a.sisi)
print("Sisi b:", b.sisi)

a.sisi = 4
print("Sisi a setelah diubah:", a.sisi)
print("Luas a sekarang:", a.luas())
print("Sisi b tidak berubah:", b.sisi)
