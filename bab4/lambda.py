salam = lambda: "Halo, Dunia!"
print(salam())

kuadrat = lambda x: x**2
print(kuadrat(5))
print(kuadrat(10))

luas_persegi_panjang = lambda p, l: p * l
print(luas_persegi_panjang(10, 5))

status_nilai = lambda n: "Lulus" if n >= 75 else "Tidak Lulus"
print(status_nilai(85))
print(status_nilai(60))

print("-" * 30)

mahasiswa = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Fajri", "nilai": 92},
    {"nama": "Andi", "nilai": 78},
]

urut_nilai = sorted(mahasiswa, key=lambda m: m["nilai"])
for m in urut_nilai:
    print(f"{m['nama']}: {m['nilai']}")
