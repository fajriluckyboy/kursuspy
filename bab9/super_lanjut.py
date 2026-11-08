#!/usr/bin/env python3
"""super() lanjutan: urutan, bentuk lengkap, dan dua jebakan.

Percobaan 1: super() di tengah, tambahan sebelum dan sesudah.
Percobaan 2: tambahan di depan untuk menyiapkan argumen.
Percobaan 3: bentuk lengkap super(Kelas, self).
Percobaan 4: jebakan lupa super().
Percobaan 5: jebakan memanggil self.metode() milik sendiri.
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


class GiroLog(Rekening):
    """Tambahan sebelum dan sesudah super(), untuk melihat urutan."""

    def tarik(self, jumlah):
        """Cetak penanda di kedua sisi pemanggilan induk."""
        print("  anak : sebelum super()")
        super().tarik(jumlah)
        print("  anak : sesudah super()")


class TabunganRapi(Rekening):
    """Menyiapkan argumen DULU, baru menyerahkan ke induk."""

    def tarik(self, jumlah):
        """Terima angka atau teks angka; induk hanya mengerti angka."""
        # Tambahan di depan: int("100") menjadi 100
        super().tarik(int(jumlah))


class Tabungan(Rekening):
    """Bentuk singkat super()."""

    def ringkas(self):
        """Label di depan ringkasan induk."""
        return f"[Tabungan] {super().ringkas()}"


class TabunganEksplisit(Rekening):
    """Bentuk lengkap super(Kelas, self); hasil sama."""

    def ringkas(self):
        """Label di depan ringkasan induk."""
        return f"[Tabungan] {super(TabunganEksplisit, self).ringkas()}"


class GiroLupa(Rekening):
    """JEBAKAN 1: override tarik() tanpa super() dan tanpa aturan."""

    BIAYA_ADMIN = 500

    def tarik(self, jumlah):
        """Menulis ulang sendiri; pemeriksaan saldo ikut hilang."""
        self.saldo -= jumlah + self.BIAYA_ADMIN


class GiroBenar(Rekening):
    """Versi benar: super() dulu agar aturan induk tetap berlaku."""

    BIAYA_ADMIN = 500

    def tarik(self, jumlah):
        """Aturan induk dulu, baru biaya admin."""
        super().tarik(jumlah)
        self.saldo -= self.BIAYA_ADMIN


class TabunganRekursi(Rekening):
    """JEBAKAN 2: memanggil self.ringkas() di dalam ringkas()."""

    def ringkas(self):
        """self.ringkas() mencari mulai dari anak: ketemu DIRINYA."""
        return "[Tabungan] " + self.ringkas()


def percobaan_urutan():
    """Percobaan 1: urutan sebelum dan sesudah super()."""
    print("== Percobaan 1: urutan ==")
    g = GiroLog("Sari", 100)
    g.tarik(30)
    print("Saldo setelah tarik 30 :", g.saldo)
    try:
        g.tarik(999)
    except ValueError as e:
        print("Ditolak                :", e)


def percobaan_siapkan():
    """Percobaan 2: tambahan di depan menyiapkan argumen."""
    print("== Percobaan 2: siapkan argumen ==")
    r = Rekening("Budi", 500)
    try:
        r.tarik("100")
    except TypeError as e:
        print("Rekening tarik('100')  : TypeError:", e)

    t = TabunganRapi("Fajri", 500)
    t.tarik("100")
    print("TabunganRapi tarik('100'):", t.saldo)


def percobaan_bentuk():
    """Percobaan 3: bentuk singkat dan bentuk lengkap."""
    print("== Percobaan 3: bentuk lengkap ==")
    a = Tabungan("Fajri", 100)
    b = TabunganEksplisit("Fajri", 100)
    print("singkat                :", a.ringkas())
    print("lengkap                :", b.ringkas())
    print("Hasil sama?            :", a.ringkas() == b.ringkas())


def percobaan_lupa():
    """Percobaan 4: lupa super() menghilangkan aturan induk."""
    print("== Percobaan 4: lupa super() ==")
    lupa = GiroLupa("Sari", 1000)
    lupa.tarik(5000)
    print("GiroLupa saldo         :", lupa.saldo)

    benar = GiroBenar("Sari", 1000)
    try:
        benar.tarik(5000)
    except ValueError as e:
        print("GiroBenar ditolak      :", e)
    print("GiroBenar saldo        :", benar.saldo)


def percobaan_rekursi():
    """Percobaan 5: metode memanggil dirinya sendiri."""
    print("== Percobaan 5: memanggil diri sendiri ==")
    t = TabunganRekursi("Fajri", 100)
    try:
        t.ringkas()
    except RecursionError as e:
        print("Jenis error            :", type(e).__name__)
        print("Awal pesan             :", str(e)[:35])


def main():
    """Alur utama program."""
    percobaan_urutan()
    percobaan_siapkan()
    percobaan_bentuk()
    percobaan_lupa()
    percobaan_rekursi()


if __name__ == "__main__":
    main()
