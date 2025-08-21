import os
import time
import pandas as pd

file_path = "database/data.csv"

# View Gadget
def view_gadget(file_path):
    # Membaca file CSV
    df = pd.read_csv(file_path, index_col="id")
    columns = ["brand", "nama_laptop", "processor", "vga", "harga"]
    view_columns = df[columns]
    # Menampilkan DataFrame
    print(view_columns)

# Search Gadget
def cari_item_csv(file_path, target_keyword):
    try:
        # Membaca file CSV ke dalam DataFrame
        df = pd.read_csv(file_path, index_col="id")

        # Menerapkan pencarian menggunakan pandas
        matching_rows = []  # Inisialisasi list untuk menyimpan baris yang cocok

        # Loop melalui setiap baris DataFrame
        for index, row in df.iterrows():
            # Loop melalui setiap sel dalam baris
            for cell in row:
                # Pemeriksaan kata kunci pencarian
                if target_keyword.lower() in str(cell).lower():
                    matching_rows.append(row)  # Menambahkan baris yang cocok ke dalam list
                    matching_rows[-1]["id"] = index  # Menambahkan kolom "id" ke dalam baris terakhir
                    break  # Keluar dari loop jika sudah menemukan satu sel yang cocok

        result_df = pd.DataFrame(matching_rows, columns=df.columns)  # Membuat DataFrame dari list

        # Menampilkan hasil pencarian
        if not result_df.empty:
            return result_df  # Menampilkan DataFrame jika ada hasil
        else:
            return pd.DataFrame()
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        return pd.DataFrame()
# Sort Gadget Search
def sort_search_gadget(result, pilihan):
    if pilihan == 1:
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara ascending
        df_sorted = result.sort_values(by='harga')
        # Menampilkan hasil
        return df_sorted

    elif pilihan == 2:
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara descending
        df_sorted = result.sort_values(by='harga', ascending=False)
        # Menampilkan hasil
        return df_sorted

# Sort Gadget View
def sort_view_gadget(file_path, pilihan):
    if pilihan == 1:
        df = pd.read_csv(file_path, index_col="id")
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara ascending
        df_sorted = df.sort_values(by='harga')
        # Menampilkan hasil
        return df_sorted

    elif pilihan == 2:
        df = pd.read_csv(file_path, index_col="id")
         # Mengurutkan DataFrame berdasarkan kolom 'harga' secara descending
        df_sorted = df.sort_values(by='harga', ascending=False)
        # Menampilkan hasil
        return df_sorted

# Detail Gadget Search
def detail_search(df, selected_id):
    # Input untuk memilih satu baris berdasarkan ID
    if selected_id and selected_id.isdigit():
        selected_row = df[df.index == int(selected_id)]  # Menggunakan index sebagai alternatif
        if not selected_row.empty:
            # Menampilkan informasi dengan format yang diinginkan
            print("\nInformasi Laptop:")
            print(f"Brand: {selected_row['brand'].values[0]}")
            print(f"Nama Laptop: {selected_row['nama_laptop'].values[0]}")
            print(f"Processor: {selected_row['processor'].values[0]}")
            print(f"VGA: {selected_row['vga'].values[0]}")
            print(f"RAM: {selected_row['ram'].values[0]}")
            print(f"Penyimpanan: {selected_row['storage'].values[0]}")
            print(f"Monitor: {selected_row['monitor'].values[0]}")
            print(f"Harga: {selected_row['harga'].values[0]}")
        else:
            #Jika ID yang di inputkan tidak ada
            print(f"==[!]== Tidak ada baris dengan ID {selected_id} ==[!]==")
    else:
        #jika memasukan inputan yang tidak valid
        clear()
        print("==[!]== ID yang dimasukkan tidak valid ==[!]==")

# Detail Gadget View
def detail_view(df, selected_id, columns=None):
    # Input untuk memilih satu baris berdasarkan ID
    if selected_id and selected_id.isdigit():
        selected_row = df[df['id'] == int(selected_id)]
        if not selected_row.empty:
            # Menampilkan informasi dengan format yang diinginkan
            print(f"Detail Laptop dengan ID {selected_id}:")
            
            if columns is None:
                # Jika tidak ada kolom yang ditentukan, tampilkan semua kolom
                columns = df.columns.tolist()
            
            for column in columns:
                # Cetak setiap kolom dan nilai di baris yang dipilih
                print(f"{column.title()}: {selected_row[column].values[0]}")
        else:
            #Jika ID yang di inputkan tidak ada
            print(f"==[!]== Tidak ada baris dengan ID {selected_id} ==[!]==")
    else:
        #jika memasukan inputan yang tidak valid
        clear()
        print("==[!]== ID yang dimasukkan tidak valid ==[!]==")

# Opsi Search
def opsi_search():
    while True:
        clear()
        print("][==========][ Cari Gadget ][==========][\n")
        target_keyword = input("Masukan Kata Kunci: ")
        result = cari_item_csv(file_path, target_keyword)

        if not result.empty:
            search_success(result)
        else:
            search_fail(target_keyword)
            continue
        
        print("\n1. Urutkan Berdasarkan Harga")
        print("2. Cek Detail Gadget")
        print("3. Kembali")

        pilihan = input("\nMasukan pilihan: ")

        if pilihan == "1":
            opsi_sort_search(result)
        elif pilihan == "2":
            opsi_detail_search(result)
        elif pilihan == "3":
            break
        else:
            error_handling()
        break  
# Opsi View
def opsi_view():
    while True:
        clear()
        print("][==========][ List Gadget ][==========][\n")
        view_gadget(file_path)
        print("\n1. Urutkan Berdasarkan Harga")
        print("2. Cek Detail Gadget")
        print("3. Kembali")

        pilihan = input("\nMasukan pilihan: ")

        if pilihan == "1":
            opsi_sort_view()
        elif pilihan == "2":
            opsi_detail_view()
        elif pilihan == "3":
            
            break
        else:
            error_handling()
        
# Opsi Sort Search
def opsi_sort_search(result):
    while True:
        print("][==========][ Hasil Pencarian ][==========][\n")
        print(result[["brand", "nama_laptop", "processor", "vga", "harga"]])
        
        print("\n1. Urutkan Berdasarkan Harga Terendah")
        print("2. Urutkan Berdasarkan Harga Tertinggi")
        print("3. Kembali")

        pilihan = input("\nMasukan pilihan: ")

        if pilihan == "1":
            sort_asc_search(result)
        elif pilihan == "2":
            sort_desc_search(result)
        elif pilihan == "3":
            break
        else:
            error_handling()

# Opsi Sort View
def opsi_sort_view():
    while True:
        clear()
        print("1. Urutkan Berdasarkan Harga Terendah")
        print("2. Urutkan Berdasarkan Harga Tertinggi")
        print("3. Kembali")
        pilihan = input("\nMasukan pilihan: ")

        if pilihan == "1":
            sort_asc_view()
        elif pilihan == "2":
            sort_desc_view()
        elif pilihan == "3":
            break
        else:
            error_handling()

# Opsi Detail Search
def opsi_detail_search(result):
    id = input("\nMasukan id berdasarkan gadget yang dipilih: ")
    detail_search(result, id)
    input("\nTekan enter untuk kembali....")

# Opsi Detail View
def opsi_detail_view():
    id = input("\nMasukan id berdasarkan gadget yang dipilih: ")
    clear()
    df = pd.read_csv(file_path)
    selected_columns = ['brand', 'nama_laptop', 'processor', 'vga', 'monitor', 'harga']
    detail_view(df, id, selected_columns)
    input("\nTekan enter untuk kembali....")

# Clear Terminal
def clear():
    os.system("cls")

# Error Handling
def error_handling():
    clear()
    print("==[!]== Masukan Inputan Yang Valid! ==[!]==")
    time.sleep(2)

# Sort Asc Search
def sort_asc_search(result):
    print("][==========][ Harga Terendah ][==========][\n")
    hasil = sort_search_gadget(result, 1)
    print(hasil)
    input("\nTekan enter untuk kembali....")

# Sort Desc Search
def sort_desc_search(result):
    print("][==========][ Harga Tertinggi ][==========][\n")
    hasil = sort_search_gadget(result, 2)
    print(hasil)
    input("\nTekan enter untuk kembali....")

# Sort Asc View
def sort_asc_view():
    clear()
    hasil = sort_view_gadget(file_path, 1)
    print(hasil)
    input("\nTekan enter untuk kembali....")

# Sort Desc View
def sort_desc_view():
    clear()
    hasil = sort_view_gadget(file_path, 2)
    print(hasil)
    input("\nTekan enter untuk kembali....")

# Search Success
def search_success(result):
    print("][==========][ Hasil Pencarian ][==========][\n")
    print(result[["brand", "nama_laptop", "processor", "vga", "harga"]])

# Search Fail
def search_fail(target_keyword):
    print(f"==[!]== Tidak Ditemukan Laptop {target_keyword} ==[!]==\n")
    input("Tekan enter untuk kembali....")