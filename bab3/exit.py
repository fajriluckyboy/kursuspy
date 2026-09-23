while True:
    print("1. Sapa")
    print("2. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        print(f"Halo, {nama}!")
    elif pilihan == "2":
        print("Sampai jumpa!")
        exit()
    else:
        print("Pilihan tidak valid, coba lagi")
