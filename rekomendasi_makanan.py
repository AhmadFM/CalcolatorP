
import pandas as pd
import random as rng

KelompokMakanan = ["Daging", "Ikan/Kerang/Udang", "Kacang-Kacangan", "Buah", "Sayuran"]

# Membaca data dari file CSV
DataBaseMakanan = pd.read_csv("database1.csv")

# Fungsi untuk menghitung kalori batas berdasarkan Tujuan pengguna
def hitung_batas(KaloriHarian, Tujuan):
    if Tujuan == "turun":
        return KaloriHarian * 0.9
    elif Tujuan == "tetap":
        return KaloriHarian
    elif Tujuan == "naik":
        return KaloriHarian * 1.1
    else:
        return KaloriHarian  

# Fungsi untuk memberikan rekomendasi menu
def rekomendasi_menu(Kategori, KaloriHarian, Tujuan):
    # Hitung batas kalori
    Batas = hitung_batas(KaloriHarian, Tujuan)
    
    filtered_df = DataBaseMakanan[DataBaseMakanan["Kategori"].str.lower() == Kategori.lower()].sort_values("Kalori")

    
    if filtered_df.empty:
        print(f"Tidak ada makanan dalam kategori {Kategori}.")
        return None

    # Pilih makanan utama (kalori terendah)
    Karbo = filtered_df[filtered_df['Kelompok'].str.lower() == 'serealia']
    if Karbo.empty:
        print(f"Tidak ada makanan dalam kategori {Kategori}.")
        return None
    Utama = Karbo.sample(frac=1, # Frac=1 untuk mengacak data 
                          ).reset_index(drop=True) # reset_index untuk mengatur ulang index
    Utama = Utama.iloc[-1]
    
    # Daftar Makanan Tambahan 
    Other = filtered_df[filtered_df['Kelompok'].str.lower() != 'serealia']
    Other = Other.sample(frac=1, # Frac=1 untuk mengacak data 
                          ).reset_index(drop=True) # reset_index untuk mengatur ulang index
    

    # Cari makanan tambahan
    MakananLainnya = []
    SisaKalori = Batas - Utama['Kalori']
    for _, Makanan in Other.iterrows():
        if Makanan["Kalori"] <= SisaKalori:
            MakananLainnya.append(Makanan["Nama Makanan"])
            SisaKalori -= Makanan["Kalori"]

    return {
        'Kategori': Kategori,
        'Makanan Utama': Utama["Nama Makanan"],
        'Kalori Utama': Utama["Kalori"],
        'Makanan Pilihan': MakananLainnya[:5]
    }

# Input dari pengguna
def recMakanan():
    try:
        # Meminta input dari pengguna
        Kategori = input("Pilih kategori menu (Sarapan, Makan Siang, Makan Malam): ").strip().lower()
        if Kategori not in ['sarapan', 'makan siang', 'makan malam']:
            print("Kategori tidak valid. Pilih dari: Sarapan, Makan Siang, Makan Malam.")
            return

        KaloriHarian = int(input("Masukkan kalori harian Anda: "))
        Tujuan = input("Masukkan Tujuan Anda (turun, tetap, naik): ").strip().lower()

        if Tujuan not in ["turun", "tetap", "naik"]:
            print("Tujuan tidak valid.")
            return
        
        # Memanggil fungsi rekomendasi menu
        Hasil = rekomendasi_menu(Kategori, KaloriHarian, Tujuan)
        if Hasil:
            print("\nRekomendasi Menu:")
            for k, v in Hasil.items():
                print(f"{k}: {v}")
        else:
            print("Tidak ada rekomendasi yang sesuai.")
    except ValueError:
        print("Input tidak valid. Pastikan kalori harian berupa angka.")

# Jalankan program utama
if __name__ == "__main__":
    recMakanan()