def pangkat(basis, eksponen, /):
    """Menghitung pangkat — parameter hanya boleh posisional."""
    return basis**eksponen


print(pangkat(2, 8))
print(pangkat(3, 4))

print("-" * 30)


def buat_koneksi(host, port, *, timeout=30, retry=3):
    """
    Membuat koneksi ke server.
    host dan port → posisional atau nama.
    timeout dan retry → wajib dengan nama.
    """
    print(f"Host    : {host}")
    print(f"Port    : {port}")
    print(f"Timeout : {timeout}s")
    print(f"Retry   : {retry}x")


buat_koneksi("localhost", 5432, timeout=60, retry=5)
print("-" * 30)
buat_koneksi("192.168.1.1", 3306)

print("-" * 30)


def proses_data(sumber, format_input, /, mode="read", *, encoding="utf-8", debug=False):
    """
    Memproses data dari sumber tertentu.
    sumber, format_input → hanya posisional.
    mode               → bebas posisional atau nama.
    encoding, debug    → wajib dengan nama.
    """
    print(f"Sumber       : {sumber}")
    print(f"Format Input : {format_input}")
    print(f"Mode         : {mode}")
    print(f"Encoding     : {encoding}")
    print(f"Debug        : {debug}")


proses_data("data.csv", "csv", mode="write", encoding="utf-8", debug=True)
