# main.py
import pandas as pd
from profil import profil, kebutuhanKaloriHarian
from kalkulator import kalkulator
from informasi_kalori import daftarInformasiKalori
from rekomendasiMakanan import rekomendasi_menu


def menu_utama():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Total Kalori Makanan")
    print("3. Informasi Kalori Makanan")
    print("4. Rekomendasi Makanan")
    print("5. Keluar")

# def opsi_menu(profilUser ):
#     pilihan = input("Pilih opsi (1-5): ")
#     if pilihan == '1':
#         profilUser  = profil(profilUser)
#     elif pilihan == '2':
#         kalkulator()
#     elif pilihan == '3':
#         daftarInformasiKalori()
#     elif pilihan == '4':
#         # hitung_batas_kalori()
#         rekomendasi_menu(kategori_menu, kalori_harian, tujuan)
#         if profilUser :
#             # Ambil kebutuhan kalori harian
#             kalori_harian = kebutuhanKaloriHarian(profilUser ['jenisKelamin'], profilUser ['berat'], profilUser ['tinggi'], profilUser ['umur'], profilUser ['skalaAktivitas'], profilUser ['target'])
#             # Input kategori menu
#             kategori_menu = input("Pilih kategori menu (sarapan/makan siang/makan malam): ").lower()
#             kategori_menu = kategori_menu.capitalize()
#             # Panggil fungsi rekomendasi menu
#             rekomendasi = rekomendasi_menu(profilUser ['target'], kalori_harian, kategori_menu)
#             if rekomendasi:
#                 print("\n==== Rekomendasi Makanan ====")
#                 print(f"Karbohidrat: {rekomendasi['Kelompok']}")
#                 print(f"Makanan Lain: {', '.join(rekomendasi['Makanan Lain'])}")
#         else:
#             print("Silahkan buat profil terlebih dahulu")
#     elif pilihan == '5':
#         print("=== Exit ===")
#         return profilUser , True  # Menandakan bahwa pengguna memilih keluar
#     else:
#         print("Pilihan tidak valid. Silakan coba lagi.")
#     return profilUser , False
# # Menandakan bahwa pengguna tidak memilih keluar
def opsi_menu(profilUser):
    pilihan = input("Pilih opsi (1-5): ")
    
    if pilihan == '1':
        profilUser = profil(profilUser)
    elif pilihan == '2':
        kalkulator()
    elif pilihan == '3':
        daftarInformasiKalori()
    elif pilihan == '4':
        # Pastikan profilUser sudah ada
        if profilUser:
            # Ambil kebutuhan kalori harian
            kalori_harian = kebutuhanKaloriHarian(
                profilUser['jenisKelamin'], 
                profilUser['berat'], 
                profilUser['tinggi'], 
                profilUser['umur'], 
                profilUser['skalaAktivitas'], 
                profilUser['target']
            )
            
            # Input kategori menu
            kategori_menu = input("Pilih kategori menu (sarapan/makan siang/makan malam): ").lower()
            kategori_menu = kategori_menu.capitalize()  # Menyusun kategori menjadi format yang sesuai

            # Input tujuan (untuk menambah kalori harian sesuai target pengguna)
            tujuan = profilUser['target']  # Misalnya 'naik', 'tetap', atau 'turun'

            # Panggil fungsi rekomendasi menu dengan 3 argumen yang diperlukan
            rekomendasi = rekomendasi_menu(kategori_menu, kalori_harian, tujuan)
            
            if rekomendasi:
                print("\n==== Rekomendasi Makanan ====")
                print(f"Kelompok: {rekomendasi['Kategori']}")
                print(f"Makanan Utama: {rekomendasi['Makanan Utama']}")
                print(f"Kalori Utama: {rekomendasi['Kalori Utama']}")
                print(f"Makanan Tambahan: {', '.join(rekomendasi['Makanan Tambahan'])}")
        else:
            print("Silahkan buat profil terlebih dahulu.")
    elif pilihan == '5':
        print("=== Exit ===")
        return profilUser, True  # Menandakan bahwa pengguna memilih keluar
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    return profilUser, False


def main():
    profilUser  = {}
    while True:
        menu_utama()
        profilUser , keluar = opsi_menu(profilUser)  # Menerima nilai `keluar` dari opsi_menu
        if keluar:
            if input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
                break

main()