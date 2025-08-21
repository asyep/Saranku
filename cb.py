import pandas as pd

def view_gadget(file_path):
    # Membaca file CSV
    df = pd.read_csv(file_path, index_col="id")
    columns = ["brand", "nama_laptop", "processor", "vga", "harga"]
    view_columns = df[columns]
    # Menampilkan DataFrame
    print(view_columns)
file_path = "database/data.csv"
rawr = view_gadget(file_path)
print(rawr)