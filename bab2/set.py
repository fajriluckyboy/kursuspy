buah = {"apel", "mangga", "jeruk"}
print(type(buah))

data = {1, 2, 2, 3, 3, 3, 4}
print(data)

list_duplikat = [1, 2, 2, 3, 3, 4]
unik = set(list_duplikat)
print(unik)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a & b)
print(a - b)

print("apel" in buah)
print("pisang" in buah)
