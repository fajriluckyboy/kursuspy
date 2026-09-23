for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

n = 0
while n < 10:
    n += 1
    if n == 5:
        continue
    print(n)

for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("selesai break")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("selesai continue")
