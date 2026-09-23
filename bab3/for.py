buah = ["apel", "mangga", "jeruk"]
for b in buah:
    print(b)

for huruf in "Fajri":
    print(huruf)

for i in range(5):
    print(i)

for i in range(0, 11, 2):
    print(i)

angka = [1, 2, 3, 4, 5]
total = 0
for n in angka:
    total += n
print(f"Total: {total}")

biodata = {"nama": "Fajri", "umur": 20, "kota": "Makassar"}
for kunci in biodata:
    print(f"{kunci}: {biodata[kunci]}")
