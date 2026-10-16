# evaluasi ekspresi matematika dasar
print("=== Ekspresi Matematika ===")
print(eval("2 + 3"))
print(eval("10 * 5"))
print(eval("100 / 4"))
print(eval("2 ** 8"))

# eval dengan variabel lokal
print("=== eval dengan Variabel ===")
x = 10
y = 20
print(eval("x + y"))
print(eval("x * y"))

# tipe hasil eval mengikuti ekspresi
print("=== Tipe Hasil eval ===")
print(type(eval("100")))
print(type(eval("3.14")))
print(type(eval("[1, 2, 3]")))
print(type(eval("{'a': 1}")))

# kalkulator sederhana
print("=== Kalkulator ===")
ekspresi = input("Masukkan ekspresi: ")
hasil = eval(ekspresi)
print(f"Hasil: {hasil}")
