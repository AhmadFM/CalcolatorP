# kalkulator.py
from database import databaseKalori

totalKalori = 0
listMakanan = []

def kalkulator():
    global totalKalori
    totalKalori = 0 
    listMakanan.clear()
   
    print("\n==== KALKULATOR KALORI ====")
    jumlahMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    i = 0  # Counter untuk loop

    while i < jumlahMakanan:
        namaMakanan = input("Masukkan nama makanan: ")

        if namaMakanan in databaseKalori: 
            listMakanan.append(namaMakanan)
            totalKalori += databaseKalori[namaMakanan]
            i += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{namaMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")

    print(f"Total kalori yang Anda makan dari {listMakanan} adalah {totalKalori} kkal")