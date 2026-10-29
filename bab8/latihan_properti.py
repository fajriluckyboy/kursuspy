class Barang:
    def __init__(self, harga):
        self.harga = harga  # mengubah self._harga menjadi self.harga

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai < 0:
            raise ValueError("Nilai tidak boleh negatif")

        self._harga = nilai


barang = Barang(5000)
print("Harga awal:", barang.harga)

barang.harga = 7500
print("Harga baru:", barang.harga)

try:
    barang.harga = -100
except ValueError as e:
    print("Ditolak:", e)

print("Harga tetap:", barang.harga)

# Percobaan: objek dibuat dengan harga negatif yang salah
# buruk = Barang(-5)
# print("Harga buruk:", buruk.harga)
#
# Percobaan: objek dengan harga negatif harus batal dibuat
try:
    buruk = Barang(-5)
    print("Harga buruk:", buruk.harga)
except ValueError as e:
    print("Gagal dibuat:", e)
