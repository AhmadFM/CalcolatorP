# # import pandas as pd

# # def rekomendasi_makanan(target, kalori_harian, kategori):
# #     data = pd.read_csv("database.csv")

# #     faktor = 0.9 if target == 'turun' else 1.1 if target == 'tetap' else 1.1

# #     limit_kalori = kalori_harian * faktor

# #     skala_kategori = {
# #         "sarapan" : 0.3,
# #         "makan siang" : 0.4,
# #         "makan malam " : 0.3
# #     }

# #     if kategori in skala_kategori:
# #         batas_kalori = limit_kalori * skala_kategori[kategori]
# #     else:
# #         print("kategori tidak valid")
# #         return None
    
# #     karbohidrat = data[data['Kelompok'] == 'Serelia']
# #     karbohidrat_rekomendasi = karbohidrat[karbohidrat['Kalori'] <= batas_kalori]

# #     sisa_kalori = batas_kalori - karbohidrat_rekomendasi['Kalori'].values[0]

# #     makanan_lain = data[data['Kalori'] <= sisa_kalori]

# #     menu_rekomendasi = {
# #         "Karbohidrat": karbohidrat_rekomendasi ['Nama Makanan'].values[0],
# #         "Makanan lain": makanan_lain ['Nama Makanan'].tolist()
# #     }

# #     return menu_rekomendasi

# import pandas as pd

# DataBaseMakanan = pd.read_csv("database.csv")


# # Fungsi untuk menghitung kalori batas berdasarkan tujuan pengguna
# def hitung_batas_kalori(kalori_harian, tujuan):
#     if tujuan == "turun":
#         return kalori_harian * 0.9
#     elif tujuan == "tetap":
#         return kalori_harian
#     elif tujuan == "naik":
#         return kalori_harian * 1.1
#     else:
#         return kalori_harian  

# def rekomendasi_menu(kelompok, kalori_harian, tujuan):
#     # Menghitung batas kalori
#     batas_kalori = hitung_batas_kalori(kalori_harian, tujuan)
    
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

#     batas_kalori_menu = batas_kalori * kelompok_menu[kelompok]
    
#     # Memilih 1 jenis makanan dari kelompok yang dipilih
#     filtered_df = DataBaseMakanan[DataBaseMakanan["Kelompok"].str.lower() == kelompok.lower()].sort_values("Kalori")
    
#     # Cek jika DataFrame tidak kosong sebelum mengambil data pertama
#     if filtered_df.empty:
#         print(f"Tidak ada makanan dalam kategori {kelompok}.")
#         return None
#     makanan_terpilih = filtered_df.iloc[0]
   
#     # Menentukan makanan lainnya sesuai dengan sisa kalori
#     sisa_kalori = batas_kalori_menu - makanan_terpilih["Kalori"]
#     makanan_lainnya = []
#     for idx, makanan in DataBaseMakanan.iterrows():
#         if makanan["Kelompok"].lower() != kelompok.lower():
#             if makanan["Kalori"] <= sisa_kalori:
#                 makanan_lainnya.append(makanan)
#                 sisa_kalori -= makanan["Kalori"]
    
#     # Mengembalikan dictionary dengan rekomendasi
#     return {
#         'Kelompok': kelompok,
#         'Makanan Lain': [makanan['Nama Makanan'] for makanan in makanan_lainnya]
#     }

# # Input dari pengguna
# def recMakanan():
#     # Input kelompok makanan
#     kelompok = input("Pilih kelompok menu (Sarapan, Makan Siang, Makan Malam): ").strip().lower()
#     kelompok = kelompok.capitalize()  # Mengubah input menjadi format yang benar
    
#     if kelompok not in ['Sarapan', 'Makan Siang', 'Makan Malam']:
#         print("Kelompok tidak valid.")
#         return

#     # Input kalori harian dan tujuan pengguna
#     kalori_harian = int(input("Masukkan kalori harian Anda: "))
#     tujuan = input("Masukkan tujuan Anda (turun, tetap, naik): ").strip().lower()

#     if tujuan not in ["turun", "tetap", "naik"]:
#         print("Tujuan tidak valid.")
#         return
    
#     # Memberikan rekomendasi menu
#     rekomendasi_menu(kelompok, kalori_harian, tujuan)

# # Jalankan program utama
# if __name__ == "__main__":
#     recMakanan() 
import pandas as pd

# Membaca data dari file CSV
DataBaseMakanan = pd.read_csv("database1.csv")


# Fungsi untuk menghitung kalori batas berdasarkan tujuan pengguna
def hitung_batas_kalori(kalori_harian, tujuan):
    if tujuan == "turun":
        return kalori_harian * 0.9
    elif tujuan == "tetap":
        return kalori_harian
    elif tujuan == "naik":
        return kalori_harian * 1.1
    else:
        return kalori_harian  

# Fungsi untuk memberikan rekomendasi menu
def rekomendasi_menu(kategori, kalori_harian, tujuan):
    # Hitung batas kalori
    batas_kalori = hitung_batas_kalori(kalori_harian, tujuan)
    
    filtered_df = DataBaseMakanan[DataBaseMakanan["Kategori"].str.lower() == kategori.lower()].sort_values("Kalori")

    
    if filtered_df.empty:
        print(f"Tidak ada makanan dalam kategori {kategori}.")
        return None

    # Pilih makanan utama (kalori terendah)
    makanan_terpilih = filtered_df.iloc[0]

    # Cari makanan tambahan
    makanan_lainnya = []
    sisa_kalori = batas_kalori - makanan_terpilih["Kalori"]
    for _, makanan in filtered_df.iterrows():
        if makanan["Kalori"] <= sisa_kalori:
            makanan_lainnya.append(makanan["Nama Makanan"])
            sisa_kalori -= makanan["Kalori"]

    return {
        'Kategori': kategori,
        'Makanan Utama': makanan_terpilih["Nama Makanan"],
        'Kalori Utama': makanan_terpilih["Kalori"],
        'Makanan Tambahan': makanan_lainnya
    }

# Input dari pengguna
def recMakanan():
    try:
        # Meminta input dari pengguna
        kategori = input("Pilih kategori menu (Sarapan, Makan Siang, Makan Malam): ").strip().lower()
        if kategori not in ['sarapan', 'makan siang', 'makan malam']:
            print("Kategori tidak valid. Pilih dari: Sarapan, Makan Siang, Makan Malam.")
            return

        kalori_harian = int(input("Masukkan kalori harian Anda: "))
        tujuan = input("Masukkan tujuan Anda (turun, tetap, naik): ").strip().lower()

        if tujuan not in ["turun", "tetap", "naik"]:
            print("Tujuan tidak valid.")
            return
        
        # Memanggil fungsi rekomendasi menu
        hasil = rekomendasi_menu(kategori, kalori_harian, tujuan)
        if hasil:
            print("\nRekomendasi Menu:")
            for k, v in hasil.items():
                print(f"{k}: {v}")
        else:
            print("Tidak ada rekomendasi yang sesuai.")
    except ValueError:
        print("Input tidak valid. Pastikan kalori harian berupa angka.")

# Jalankan program utama
if __name__ == "__main__":
    recMakanan()

