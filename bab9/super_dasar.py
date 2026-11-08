#!/usr/bin/env python3
"""super() pada metode biasa: memperluas perilaku induk.

Induk   : Rekening (ringkas, tarik)
Anak 1  : Tabungan (ringkas diperluas: induk dulu, lalu label)
Anak 2  : Giro     (tarik diperluas: induk dulu, lalu biaya admin)
Anak 3  : TabunganLama (ringkas lewat nama induk, bandingan)
"""


class Rekening:
    """Kelas induk: aturan umum rekening."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def ringkas(self):
        """Kontrak: mengembalikan teks ringkasan."""
        return f"{self.pemilik}: Rp{self.saldo}"

    def tarik(self, jumlah):
        """Kurangi saldo; tidak boleh melebihi saldo."""
        if jumlah > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= jumlah


class Tabungan(Rekening):
    """Anak 1: ringkas() memperluas milik induk."""

    def ringkas(self):
        """Ambil ringkasan induk, lalu tambahkan label di depannya."""
        # super().ringkas() = ringkas milik Rekening, untuk self ini
        dasar = super().ringkas()
        return f"[Tabungan] {dasar}"

    def jenis_perantara(self):
        """Untuk pengamatan: apa sebenarnya hasil super()?"""
        return type(super())


class Giro(Rekening):
    """Anak 2: tarik() memperluas milik induk."""

    BIAYA_ADMIN = 500

    def tarik(self, jumlah):
        """Jalankan aturan induk dulu, baru potong biaya admin."""
        # Bila induk melempar ValueError, baris di bawah tidak jalan
        super().tarik(jumlah)
        self.saldo -= self.BIAYA_ADMIN


class TabunganLama(Rekening):
    """Anak 3: hasil sama, tetapi memanggil induk lewat nama."""

    def ringkas(self):
        """Nama induk tertulis kaku dan self dikirim manual."""
        dasar = Rekening.ringkas(self)
        return f"[Tabungan] {dasar}"


def main():
    """Alur utama program."""
    print("--- Memperluas ringkas() ---")
    r = Rekening("Budi", 100)
    t = Tabungan("Fajri", 100)
    print("r.ringkas()          :", r.ringkas())
    print("t.ringkas()          :", t.ringkas())

    print("--- Dibandingkan dengan memanggil lewat nama ---")
    lama = TabunganLama("Fajri", 100)
    print("lama.ringkas()       :", lama.ringkas())
    print("Hasil sama?          :", t.ringkas() == lama.ringkas())

    print("--- Memperluas tarik(): induk dulu, lalu biaya ---")
    g = Giro("Sari", 1000)
    g.tarik(200)
    print("Setelah tarik 200    :", g.saldo)

    print("--- Aturan induk tetap berlaku ---")
    try:
        g.tarik(5000)
    except ValueError as e:
        print("Ditolak              :", e)
    print("Saldo setelah ditolak:", g.saldo)

    print("--- Apa itu hasil super()? ---")
    print("t.jenis_perantara()  :", t.jenis_perantara())

    print("--- super() di luar metode ---")
    try:
        super()
    except RuntimeError as e:
        print("RuntimeError:", e)


if __name__ == "__main__":
    main()
