angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in angka:
    if n == 5:
        break
    print(n)
print("Loop selesai")

while True:
    jawaban = input("Ketik 'keluar' untuk berhenti: ")
    if jawaban == "keluar":
        break
    print(f"Kamu mengetik: {jawaban}")
print("Program selesai")
