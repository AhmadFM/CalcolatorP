from tabulate import tabulate
import pandas as pd

# Membaca file CSV
DataBaseMakanan = pd.read_csv("database.csv")

# Mengambil kolom yang dibutuhkan
daftarMakanan = DataBaseMakanan.filter(items=['ID', 'Nama Makanan', 'Kalori'])

def daftarInformasiKalori():
    print("\n==== INFORMASI KALORI MAKANAN ====")
    
    # Input jumlah makanan
    jumlahInformasiMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))

    listMakananUser = []  # Menyimpan input nama makanan dari user

    # Loop input nama makanan
    for i in range(jumlahInformasiMakanan):
        cariMakanan = input(f"Masukkan nama makanan ke-{i + 1}: ")
        listMakananUser.append(cariMakanan)

    print("\nMencari informasi kalori...")

    # Mencari data yang sesuai dari file CSV
    tabel = []  # Menyimpan hasil pencarian
    for makanan in listMakananUser:
        hasil = DataBaseMakanan[DataBaseMakanan['Nama Makanan'].str.lower() == makanan.lower()]
        
        if not hasil.empty:  # Jika makanan ditemukan
            for _, row in hasil.iterrows():
                tabel.append([row['ID'], row['Nama Makanan'], row['Kalori']])
        else:  # Jika makanan tidak ditemukan
            tabel.append(["-", makanan, "Tidak ditemukan"])

    # Menampilkan hasil dalam bentuk tabel
    tabelMakanan = tabulate(tabel, headers=["ID", "Nama Makanan", "Kalori"], tablefmt="grid")
    print(tabelMakanan)
