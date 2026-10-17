import math

phi = 3.14


def hitung(r):
    return phi * r * r


print("File lingkaran2 dimuat")

if __name__ == "__main__":
    print("Ini hanya saat dijalankan langsung")
    r = input("Jari-jari: ")
    print(hitung(float(r)))
