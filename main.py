from function import opsi_search, opsi_view, error_handling, clear

file_path = "database/data.csv"

# Opsi
while True:
    clear()
    print("][==========][ Selamat datang di Saranku! ][==========][\n")
    print("1. Cari Gadget")
    print("2. Tampilkan Semua Gadget")
    print("3. Keluar")

    pilihan = input("\nMasukan pilihan: ")

    if pilihan == "1":
        opsi_search()
    elif pilihan == "2":
        opsi_view()
    elif pilihan == "3":
        clear()
        break
    else:
        error_handling()
        continue