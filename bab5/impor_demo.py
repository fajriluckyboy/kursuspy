print("=== Bentuk 1: import modul ===")
import matematika

print(matematika.tambah(2, 3))
print(matematika.PI)

print("=== Bentuk 2: from...import ===")
from matematika import kali, PI

print(kali(4, 5))
print(PI)

print("=== Bentuk 3: alias ===")
import matematika as mtk
from matematika import luas_lingkaran as luas

print(mtk.tambah(10, 20))
print(luas(10))

print("=== Bentuk 4: wildcard ===")
from matematika import *

print(tambah(1, 1))
