#!/usr/bin/env python3
"""Kontrak override dan tiga jebakan diamnya.

Percobaan 1: salah ketik nama (override gagal diam-diam).
Percobaan 2: parameter berbeda (kode umum gagal dengan TypeError).
Percobaan 3: jenis hasil berbeda (induk menerima None).
"""


class Rekening:
    """Kelas induk dengan kontrak: tarik(jumlah), ringkas() -> teks."""

    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def tarik(self, jumlah):
        """Kurangi saldo; tidak boleh melebihi saldo."""
        if jumlah > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= jumlah

    def ringkas(self):
        """Kontrak: mengembalikan TEKS, tidak mencetak."""
        return f"{self.pemilik}: Rp{self.saldo}"

    def cetak(self):
        """Mencetak hasil ringkas(); bergantung pada kontraknya."""
        print("Cetak:", self.ringkas())


class TabunganTypo(Rekening):
    """JEBAKAN 1: niat override ringkas(), tetapi nama salah ketik."""

    def ringkaz(self):
        """Bukan override: nama 'ringkaz' belum dipakai induk."""
        return f"[Tabungan] {self.pemilik}: Rp{self.saldo}"


class GiroBeda(Rekening):
    """JEBAKAN 2: parameter wajib tambahan, melanggar kontrak."""

    def tarik(self, jumlah, biaya):
        """Override dengan parameter 'biaya' yang WAJIB diisi."""
        total = jumlah + biaya
        if total > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= total


class GiroBenar(Rekening):
    """Versi benar: parameter tambahan punya nilai default."""

    def tarik(self, jumlah, biaya=0):
        """Override yang tetap bisa dipanggil seperti induk."""
        total = jumlah + biaya
        if total > self.saldo:
            raise ValueError("saldo tidak cukup")
        self.saldo -= total


class TabunganCetak(Rekening):
    """JEBAKAN 3: ringkas() mencetak dan mengembalikan None."""

    def ringkas(self):
        """Melanggar kontrak: induk berjanji mengembalikan teks."""
        print(f"[Tabungan] {self.pemilik}: Rp{self.saldo}")


def tarik_seragam(rek, jumlah):
    """Kode umum: hanya tahu kontrak rek.tarik(jumlah)."""
    rek.tarik(jumlah)
    return rek.saldo


def percobaan_typo():
    """Percobaan 1: salah ketik nama metode."""
    print("== Percobaan 1: salah ketik ==")
    t = TabunganTypo("Fajri", 100)
    print("t.ringkas()                   :", t.ringkas())
    print("t.ringkaz()                   :", t.ringkaz())
    print("'ringkas' in vars(TabunganTypo):", "ringkas" in vars(TabunganTypo))
    print("'ringkaz' in vars(TabunganTypo):", "ringkaz" in vars(TabunganTypo))
    t.cetak()


def percobaan_parameter():
    """Percobaan 2: parameter berbeda dari induk."""
    print("== Percobaan 2: parameter berbeda ==")
    beda = GiroBeda("Sari", 1000)
    try:
        tarik_seragam(beda, 100)
    except TypeError as e:
        print("GiroBeda lewat kode umum  : TypeError:", e)

    benar = GiroBenar("Sari", 1000)
    print("GiroBenar lewat kode umum :", tarik_seragam(benar, 100))
    benar.tarik(100, biaya=10)
    print("GiroBenar dengan biaya    :", benar.saldo)


def percobaan_kontrak():
    """Percobaan 3: jenis hasil berbeda dari induk."""
    print("== Percobaan 3: jenis hasil berbeda ==")
    c = TabunganCetak("Budi", 100)
    hasil = c.ringkas()
    print("hasil ringkas()           :", hasil)
    c.cetak()


def main():
    """Alur utama program."""
    percobaan_typo()
    percobaan_parameter()
    percobaan_kontrak()


if __name__ == "__main__":
    main()
