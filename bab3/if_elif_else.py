nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E - Tidak lulus")

umur = int(input("Masukkan umur: "))

if umur < 5:
    print("Balita")
elif umur < 13:
    print("Anak-anak")
elif umur < 18:
    print("Remaja")
elif umur < 60:
    print("Dewasa")
else:
    print("Lansia")
