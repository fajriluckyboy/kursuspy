#!/usr/bin/env python3
"""Properti lanjutan: properti terhitung, deleter, dan pedoman memilih.

Harga dan diskon DISIMPAN. Harga akhir TIDAK disimpan,
melainkan dihitung setiap kali dibaca, sehingga selalu cocok.
"""


class Produk:
    """Barang dagangan dengan harga, diskon, dan catatan."""

    def __init__(self, nama, harga, diskon=0):
        self.nama = nama
        # Dua baris ini melewati setter, jadi nilai awal ikut divalidasi
        self.harga = harga
        self.diskon = diskon
        # Catatan boleh kosong; None = belum ada catatan
        self._catatan = None

    @property
    def harga(self):
        """Getter harga normal."""
        return self._harga

    @harga.setter
    def harga(self, nilai):
        """Setter harga: tipe angka dan tidak negatif."""
        if not isinstance(nilai, (int, float)):
            raise TypeError("harga harus berupa angka")
        if nilai < 0:
            raise ValueError("harga tidak boleh negatif")
        self._harga = nilai

    @property
    def diskon(self):
        """Getter diskon dalam persen."""
        return self._diskon

    @diskon.setter
    def diskon(self, nilai):
        """Setter diskon: angka antara 0 sampai 100."""
        if not isinstance(nilai, (int, float)):
            raise TypeError("diskon harus berupa angka")
        # Perbandingan berantai (Bab 2): 0 <= nilai <= 100
        if not 0 <= nilai <= 100:
            raise ValueError("diskon harus antara 0 dan 100")
        self._diskon = nilai

    @property
    def harga_akhir(self):
        """Properti terhitung: TIDAK punya atribut penyimpan sendiri.

        Dihitung dari harga dan diskon setiap kali dibaca,
        jadi tidak mungkin lupa diperbarui.
        """
        return self._harga * (100 - self._diskon) / 100

    @property
    def catatan(self):
        """Getter catatan; None bila belum ada."""
        return self._catatan

    @catatan.setter
    def catatan(self, teks):
        """Setter catatan: harus teks."""
        if not isinstance(teks, str):
            raise TypeError("catatan harus berupa teks")
        self._catatan = teks

    @catatan.deleter
    def catatan(self):
        """Deleter: dijalankan saat del produk.catatan."""
        # Bukan menghapus atribut _catatan, tetapi mengembalikannya
        # ke keadaan awal supaya objek tetap utuh
        self._catatan = None

    def label(self):
        """Metode, bukan properti: melakukan tindakan menyusun teks."""
        return f"{self.nama} - Rp{self.harga_akhir}"


def main():
    """Alur utama program."""
    tas = Produk("Tas", 200000, 10)
    print("Harga akhir          :", tas.harga_akhir)

    # Ubah data asal: harga akhir ikut berubah tanpa ditulis ulang
    tas.harga = 300000
    print("Setelah harga naik   :", tas.harga_akhir)

    tas.diskon = 50
    print("Setelah diskon 50    :", tas.harga_akhir)
    print("Label                :", tas.label())

    # Setter menjaga rentang diskon
    try:
        tas.diskon = 150
    except ValueError as e:
        print("Ditolak (diskon)     :", e)

    # Properti terhitung tidak punya setter
    try:
        tas.harga_akhir = 1
    except AttributeError as e:
        print("Ditolak (hanya-baca) :", e)

    # Siklus hidup catatan: kosong, isi, hapus
    print("Catatan awal         :", tas.catatan)
    tas.catatan = "stok terbatas"
    print("Catatan diisi        :", tas.catatan)
    del tas.catatan
    print("Catatan setelah del  :", tas.catatan)

    # Atribut yang benar-benar tersimpan di objek
    print("Isi objek            :", vars(tas))


if __name__ == "__main__":
    main()
