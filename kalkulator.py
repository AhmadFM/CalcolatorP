# kalkulator.py
# from database import databaseKalori
import pandas as pd

data = pd.read_csv("database1.csv")
data ['Nama Makanan'] = data ['Nama Makanan'].str.lower()
databaseKalori = data.set_index('Nama Makanan').to_dict()['Kalori']

totalKalori = 0
listMakanan = []

def kalkulator():
    global totalKalori
    totalKalori = 0 
    listMakanan.clear()
   
    print("\n==== KALKULATOR KALORI ====")
    while True:
        try:
            jumlahMakanan = int(input("Masukkan jumlah Makanan yang Anda Makan: "))
        except ValueError:
            print("\nInput tidak sesuai:\nJumlah makanan harus berupa angka")
        else: break

    i = 0  # Counter untuk loop
    while i < jumlahMakanan:
        namaMakanan = str(input("Masukkan nama makanan: ")).lower()

        if namaMakanan in databaseKalori: 
            listMakanan.append(namaMakanan)
            totalKalori += databaseKalori[namaMakanan]
            i += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{namaMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")

    print(f"Total kalori yang Anda makan dari {listMakanan} adalah {totalKalori} kkal")