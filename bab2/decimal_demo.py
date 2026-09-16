from decimal import Decimal, getcontext

print(0.1 + 0.2)
print(Decimal("0.1") + Decimal("0.2"))

getcontext().prec = 10
hasil = Decimal("22") / Decimal("7")
print(hasil)

harga = Decimal("15000.50")
pajak = Decimal("0.11")
total = harga + (harga * pajak)
print(f"Total: {total}")
