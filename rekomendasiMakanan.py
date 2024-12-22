# import pandas as pd

# def rekomendasi_makanan(target, kalori_harian, kategori):
#     data = pd.read_csv("database.csv")

#     faktor = 0.9 if target == 'turun' else 1.1 if target == 'tetap' else 1.1

#     limit_kalori = kalori_harian * faktor

#     skala_kategori = {
#         "sarapan" : 0.3,
#         "makan siang" : 0.4,
#         "makan malam " : 0.3
#     }

#     if kategori in skala_kategori:
#         batas_kalori = limit_kalori * skala_kategori[kategori]
#     else:
#         print("kategori tidak valid")
#         return None
    
#     karbohidrat = data[data['Kelompok'] == 'Serelia']
#     karbohidrat_rekomendasi = karbohidrat[karbohidrat['Kalori'] <= batas_kalori]

#     sisa_kalori = batas_kalori - karbohidrat_rekomendasi['Kalori'].values[0]

#     makanan_lain = data[data['Kalori'] <= sisa_kalori]

#     menu_rekomendasi = {
#         "Karbohidrat": karbohidrat_rekomendasi ['Nama Makanan'].values[0],
#         "Makanan lain": makanan_lain ['Nama Makanan'].tolist()
#     }

#     return menu_rekomendasi

import pandas as pd

DataBaseMakanan = pd.read_csv("database.csv")


# Fungsi untuk menghitung kalori batas berdasarkan tujuan pengguna
def hitung_batas_kalori(kalori_harian, tujuan):
    if tujuan == "turun":
        return kalori_harian * 0.9
    elif tujuan == "tetap":
        return kalori_harian
    elif tujuan == "naik":
        return kalori_harian * 1.1
    else:
        return kalori_harian  # Default jika tujuan tidak valid

# Fungsi untuk memberikan rekomendasi menu
def rekomendasi_menu(kelompok, kalori_harian, tujuan):
    # Menghitung batas kalori
    batas_kalori = hitung_batas_kalori(kalori_harian, tujuan)
    
    # Menentukan batas kalori menu berdasarkan kelompok menu
    kelompok_menu = {
        'Sarapan': 0.3,
        'Makan Siang': 0.4,
        'Makan Malam': 0.3,
    }
    
    batas_kalori_menu = batas_kalori * kelompok_menu[kelompok]
    
    # Memilih 1 jenis makanan dari kelompok yang dipilih
    filtered_df = DataBaseMakanan[["Kelompok"].str.lower() == kelompok.lower()].sort_values("Kalori")
    
    # Cek jika DataFrame tidak kosong sebelum mengambil data pertama
    if not filtered_df.empty:
        makanan_terpilih = filtered_df.iloc[0]
    else:
        print(f"Tidak ada makanan dalam kelompok {kelompok}.")
        return
    
    # Menentukan makanan lainnya sesuai dengan sisa kalori
    sisa_kalori = batas_kalori_menu - makanan_terpilih["Kalori"]
    makanan_lainnya = []
    for idx, makanan in DataBaseMakanan.iterrows():
        if makanan["Kelompok"].lower() != kelompok.lower():
            if makanan["Kalori"] <= sisa_kalori:
                makanan_lainnya.append(makanan)
                sisa_kalori -= makanan["Kalori"]
    
    # Menampilkan rekomendasi menu
    print(f"\nRekomendasi menu untuk {kelompok}:")
    print(f"1. {makanan_terpilih['Nama Makanan']} ({makanan_terpilih['Kelompok']}) - Kalori: {makanan_terpilih['Kalori']}")
    for idx, makanan in enumerate(makanan_lainnya, 2):
        print(f"{idx}. {makanan['Nama Makanan']} ({makanan['Kelompok']}) - Kalori: {makanan['Kalori']}")

# Input dari pengguna
def main():
    # Input kelompok makanan
    kelompok = input("Pilih kelompok menu (Sarapan, Makan Siang, Makan Malam): ").strip().lower()
    kelompok = kelompok.capitalize()  # Mengubah input menjadi format yang benar
    
    if kelompok not in ['Sarapan', 'Makan Siang', 'Makan Malam']:
        print("Kelompok tidak valid.")
        return

    # Input kalori harian dan tujuan pengguna
    kalori_harian = int(input("Masukkan kalori harian Anda: "))
    tujuan = input("Masukkan tujuan Anda (turun, tetap, naik): ").strip().lower()

    if tujuan not in ["turun", "tetap", "naik"]:
        print("Tujuan tidak valid.")
        return
    
    # Memberikan rekomendasi menu
    rekomendasi_menu(kelompok, kalori_harian, tujuan)

# Jalankan program utama
main()
