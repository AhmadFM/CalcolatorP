from database import databaseKalori
from tabulate import tabulate

def daftarInformasiKalori():
    print("\n==== INFORMASI KALORI MAKANAN ====")

    jumlahInformasiMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    j = 0  # Counter untuk loop

    tabel = []

    while j < jumlahInformasiMakanan:
        cariMakanan = input("Masukkan nama makanan: ")

        if cariMakanan in databaseKalori:
            tabel.append([cariMakanan, databaseKalori[cariMakanan]])
            j += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{cariMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")
    
    tabelMakanan = tabulate(tabel, headers=["Nama Makanan", "Kalori"], tablefmt="grid")
    print(tabelMakanan)