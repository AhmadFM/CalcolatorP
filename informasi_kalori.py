from tabulate import tabulate
import pandas as pd

# Membaca file CSV
DATA_MAKANAN = pd.read_csv("database1.csv")

# Mengambil kolom yang dibutuhkan
DaftarMakanan = DATA_MAKANAN.filter(items=['ID', 'Nama Makanan', 'Kalori'])

def daftar_informasi_kalori():
    print("\n==== INFORMASI KALORI MAKANAN ====")
    
    # Input jumlah makanan
    JumlahMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))

    ListMakananUser = []  # Menyimpan input nama makanan dari user

    # Loop input nama makanan
    for i in range(JumlahMakanan):
        CariMakanan = input(f"Masukkan nama makanan ke-{i + 1}: ")
        ListMakananUser.append(CariMakanan)

    print("\nMencari informasi kalori...")

    # Mencari data yang sesuai dari file CSV
    Tabel = []  # Menyimpan Hasil pencarian
    for Makanan in ListMakananUser:
        Hasil = DATA_MAKANAN[DATA_MAKANAN['Nama Makanan'].str.lower() == Makanan.lower()]
        
        if not Hasil.empty:  # Jika makanan ditemukan
            for _, row in Hasil.iterrows():
                Tabel.append([row['ID'], row['Nama Makanan'], row['Kalori']])
        else:  # Jika makanan tidak ditemukan
            Tabel.append(["-", Makanan, "Tidak ditemukan"])

    # Menampilkan Hasil dalam bentuk Tabel
    TabelMakanan = tabulate(Tabel, headers=["ID", "Nama Makanan", "Kalori"], tablefmt="grid")
    print(TabelMakanan)
