# kalkulator.py
# from database import DatabaseKalori
import pandas as pd

Data = pd.read_csv("database1.csv")
Data ['Nama Makanan'] = Data ['Nama Makanan'].str.lower()
DatabaseKalori = Data.set_index('Nama Makanan').to_dict()['Kalori']

TotalKalori = 0
ListMakanan = []

def kalkulator():
    global TotalKalori
    TotalKalori = 0 
    ListMakanan.clear()
   
    print("\n==== KALKULATOR KALORI ====")
    jumlahMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    i = 0  # Counter untuk loop

    while i < jumlahMakanan:
        NamaMakanan = input("Masukkan nama makanan: ")

        if NamaMakanan in DatabaseKalori: 
            ListMakanan.append(NamaMakanan)
            TotalKalori += DatabaseKalori[NamaMakanan]
            i += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{NamaMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")

    print(f"Total kalori yang Anda makan dari {ListMakanan} adalah {TotalKalori} kkal")