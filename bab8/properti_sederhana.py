# KELAS 1: tanpa properti, atribut biasa
class OrangBiasa:
    def __init__(self, umur):
        self.umur = umur


# KELAS 2: dengan properti
class Orang:
    def __init__(self, umur):
        # self.umur (tanpa _) memanggil setter, jadi nilai awal ikut diperiksa
        self.umur = umur

    # Jalur MEMBACA: dijalankan saat orang.umur ditulis
    @property
    def umur(self):
        return self._umur

    # Jalur MENGISI: dijalankan saat orang.umur = nilai ditulis
    @umur.setter
    def umur(self, nilai):
        if nilai < 0:
            raise ValueError("umur tidak boleh negatif")
        self._umur = nilai


# Percobaan 1: atribut biasa
a = OrangBiasa(20)
a.umur = -5
print("Tanpa properti, umur a:", a.umur)

# Percobaan 2: dengan properti
b = Orang(20)
print("Dengan properti, umur b:", b.umur)

try:
    b.umur = -5
except ValueError as e:
    print("Ditolak:", e)

print("Umur b tetap:", b.umur)
