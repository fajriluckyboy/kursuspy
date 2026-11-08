#!/usr/bin/env python3
"""Override: anak menulis ulang metode induk.

Induk    : Rekening (tarik, ringkas, cetak)
Anak 1   : Tabungan (override ringkas)
Anak 2   : Giro     (override tarik: boleh minus sampai batas)
"""


class Rekening:
    """Kelas induk: aturan umum rekening."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def tarik(self, jumlah):
        """Kurangi saldo; tidak boleh melebihi saldo."""
        if jumlah > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= jumlah

    def ringkas(self):
        """Kembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"

    def cetak(self):
        """Cetak ringkasan. Memanggil self.ringkas()."""
        print("Cetak:", self.ringkas())


class Tabungan(Rekening):
    """Anak 1: menimpa ringkas() agar menyebut jenisnya."""

    def ringkas(self):
        """Override: ringkasan dengan label jenis."""
        return f"[Tabungan] {self.pemilik}: Rp{self.saldo}"


class Giro(Rekening):
    """Anak 2: menimpa tarik() agar boleh minus sampai batas."""

    # Atribut kelas milik anak (Sub-materi 2)
    BATAS_MINUS = 1000

    def tarik(self, jumlah):
        """Override: boleh melebihi saldo sampai BATAS_MINUS."""
        if jumlah > self.saldo + self.BATAS_MINUS:
            raise ValueError("melebihi batas minus")
        self.saldo -= jumlah


def coba_tarik(rek, jumlah):
    """Coba tarik dan laporkan hasilnya, apa pun jenis rekeningnya."""
    try:
        rek.tarik(jumlah)
    except ValueError as e:
        print(f"{rek.pemilik:6} tarik {jumlah}: ValueError: {e}")
    else:
        print(f"{rek.pemilik:6} tarik {jumlah}: berhasil, " f"saldo {rek.saldo}")


def main():
    """Alur utama program."""
    r = Rekening("Budi", 100)
    t = Tabungan("Fajri", 100)
    g = Giro("Sari", 100)

    print("--- Override ringkas() pada Tabungan ---")
    print("r.ringkas() :", r.ringkas())
    print("t.ringkas() :", t.ringkas())
    print("g.ringkas() :", g.ringkas())

    print("--- cetak() milik induk memanggil self.ringkas() ---")
    r.cetak()
    t.cetak()
    g.cetak()

    print("--- Override tarik() pada Giro ---")
    coba_tarik(r, 500)
    coba_tarik(t, 500)
    coba_tarik(g, 500)
    coba_tarik(g, 2000)

    print("--- Siapa pemilik metode ---")
    print("'ringkas' in vars(Tabungan):", "ringkas" in vars(Tabungan))
    print("'tarik' in vars(Tabungan)  :", "tarik" in vars(Tabungan))
    print("'tarik' in vars(Giro)      :", "tarik" in vars(Giro))

    print("--- Metode induk tetap utuh ---")
    print("Rekening.ringkas(t) :", Rekening.ringkas(t))


if __name__ == "__main__":
    main()
