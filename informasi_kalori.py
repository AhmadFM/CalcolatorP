# Daftar Informasi Kalori Makanan
from tabulate import tabulate
import pandas as pd

# Membaca file CSV
DATA_MAKANAN = pd.read_csv("database.csv")

def kategoriMakanan():
    print("1. Buah")
    print("2. Daging")
    print("3. Seafood")
    print("4. Kacang-Kacangan")
    print("5. Sayuran")
    print("6. Serealia")

def daftar_informasi_kalori():    
    # Input jumlah makanan
    kategoriMakanan()
    kategori = str(input("\nPilih Jenis Makanan yang Ingin Ada Lihat (1 - 5): "))
    if kategori == '1':
        Kelompok = 'Buah'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    elif kategori == '2':
        Kelompok = 'Daging'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    elif kategori == '3':
        Kelompok = 'Seafood'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    elif kategori == '4':
        Kelompok = 'Kacang-Kacangan'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    elif kategori == '5':
        Kelompok = 'Sayuran'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    elif kategori == '6':
        Kelompok = 'Serealia'
        Hasil = DATA_MAKANAN[DATA_MAKANAN["Kelompok"].str.lower() == Kelompok.lower()].sort_values("Nama Makanan")
    else:
        print("Input yang Anda Masukan Tidak Valid")
        return 0

    print(f"\nDaftar Makanan \"{Kelompok}\" \n")
    Show = Hasil.filter(items=['ID', 'Nama Makanan', 'Kalori'])
    TabelMakanan = tabulate(Show, headers=["ID", "Nama Makanan", "Kalori"], tablefmt="grid")
    print(TabelMakanan)
