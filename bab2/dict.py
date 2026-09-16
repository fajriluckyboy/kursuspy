biodata = {
    "nama": "Fajri",
    "umur": 20,
    "kota": "Makassar"
}
print(type(biodata))

print(biodata["nama"])
print(biodata["umur"])

biodata["pekerjaan"] = "programmer"
biodata["umur"] = 21
print(biodata)

del biodata["kota"]
print(biodata)

print("nama" in biodata)
print("alamat" in biodata)

print(len(biodata))
