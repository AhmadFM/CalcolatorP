# # import pandas as pd

# # def rekomendasi_makanan(target, KaloriHarian, Kategori):
# #     data = pd.read_csv("database.csv")

# #     faktor = 0.9 if target == 'turun' else 1.1 if target == 'tetap' else 1.1

# #     limit_kalori = KaloriHarian * faktor

# #     skala_Kategori = {
# #         "sarapan" : 0.3,
# #         "makan siang" : 0.4,
# #         "makan malam " : 0.3
# #     }

# #     if Kategori in skala_Kategori:
# #         batas = limit_kalori * skala_Kategori[Kategori]
# #     else:
# #         print("Kategori tidak valid")
# #         return None
    
# #     karbohidrat = data[data['Kelompok'] == 'Serelia']
# #     karbohidrat_rekomendasi = karbohidrat[karbohidrat['Kalori'] <= batas]

# #     SisaKalori = batas - karbohidrat_rekomendasi['Kalori'].values[0]

# #     makanan_lain = data[data['Kalori'] <= SisaKalori]

# #     menu_rekomendasi = {
# #         "Karbohidrat": karbohidrat_rekomendasi ['Nama Makanan'].values[0],
# #         "Makanan lain": makanan_lain ['Nama Makanan'].tolist()
# #     }

# #     return menu_rekomendasi

# import pandas as pd

# DataBaseMakanan = pd.read_csv("database.csv")


# # Fungsi untuk menghitung kalori batas berdasarkan Tujuan pengguna
# def hitung_batas(KaloriHarian, Tujuan):
#     if Tujuan == "turun":
#         return KaloriHarian * 0.9
#     elif Tujuan == "tetap":
#         return KaloriHarian
#     elif Tujuan == "naik":
#         return KaloriHarian * 1.1
#     else:
#         return KaloriHarian  

# def rekomendasi_menu(kelompok, KaloriHarian, Tujuan):
#     # Menghitung batas kalori
#     batas = hitung_batas(KaloriHarian, Tujuan)
    
#     # Menentukan batas kalori menu berdasarkan kelompok menu
#     kelompok_menu = {
#         'Sarapan': 0.3,
#         'Makan Siang': 0.4,
#         'Makan Malam': 0.3,
#     }
    
#     kelompok = kelompok.strip().capitalize()
    
#     # Mengubah input kelompok menjadi format yang benar
#     if kelompok not in kelompok_menu:
#         print(f"Kelompok {kelompok} tidak valid.")
#         return None

#     batas_menu = batas * kelompok_menu[kelompok]
    
#     # Memilih 1 jenis makanan dari kelompok yang dipilih
#     filtered_df = DataBaseMakanan[DataBaseMakanan["Kelompok"].str.lower() == kelompok.lower()].sort_values("Kalori")
    
#     # Cek jika DataFrame tidak kosong sebelum mengambil data pertama
#     if filtered_df.empty:
#         print(f"Tidak ada makanan dalam Kategori {kelompok}.")
#         return None
#     MakananTerpilih = filtered_df.iloc[0]
   
#     # Menentukan makanan lainnya sesuai dengan sisa kalori
#     SisaKalori = batas_menu - MakananTerpilih["Kalori"]
#     MakananLainnya = []
#     for idx, makanan in DataBaseMakanan.iterrows():
#         if makanan["Kelompok"].lower() != kelompok.lower():
#             if makanan["Kalori"] <= SisaKalori:
#                 MakananLainnya.append(makanan)
#                 SisaKalori -= makanan["Kalori"]
    
#     # Mengembalikan dictionary dengan rekomendasi
#     return {
#         'Kelompok': kelompok,
#         'Makanan Lain': [makanan['Nama Makanan'] for makanan in MakananLainnya]
#     }

# # Input dari pengguna
# def recMakanan():
#     # Input kelompok makanan
#     kelompok = input("Pilih kelompok menu (Sarapan, Makan Siang, Makan Malam): ").strip().lower()
#     kelompok = kelompok.capitalize()  # Mengubah input menjadi format yang benar
    
#     if kelompok not in ['Sarapan', 'Makan Siang', 'Makan Malam']:
#         print("Kelompok tidak valid.")
#         return

#     # Input kalori harian dan Tujuan pengguna
#     KaloriHarian = int(input("Masukkan kalori harian Anda: "))
#     Tujuan = input("Masukkan Tujuan Anda (turun, tetap, naik): ").strip().lower()

#     if Tujuan not in ["turun", "tetap", "naik"]:
#         print("Tujuan tidak valid.")
#         return
    
#     # Memberikan rekomendasi menu
#     rekomendasi_menu(kelompok, KaloriHarian, Tujuan)

# # Jalankan program utama
# if __name__ == "__main__":
#     recMakanan() 
import pandas as pd

# Membaca data dari file CSV
DataBaseMakanan = pd.read_csv("databasenew.csv")


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
    MakananTerpilih = filtered_df.iloc[0]

    # Cari makanan tambahan
    MakananLainnya = []
    SisaKalori = Batas - MakananTerpilih["Kalori"]
    for _, Makanan in filtered_df.iterrows():
        if Makanan["Kalori"] <= SisaKalori:
            MakananLainnya.append(Makanan["Nama Makanan"])
            SisaKalori -= Makanan["Kalori"]

    return {
        'Kategori': Kategori,
        'Makanan Utama': MakananTerpilih["Nama Makanan"],
        'Kalori Utama': MakananTerpilih["Kalori"],
        'Makanan Tambahan': MakananLainnya
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