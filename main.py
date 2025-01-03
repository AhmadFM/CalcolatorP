# main.py
import pandas as pd
from profil import profil, kebutuhan_kalori_harian
from kalkulator import kalkulator
from informasi_kalori import daftar_informasi_kalori
from rekomendasi_makanan import rekomendasi_menu


def menuUtama():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Total Kalori Makanan")
    print("3. Informasi Kalori Makanan")
    print("4. Rekomendasi Makanan")
    print("5. Keluar")

def opsiMenu(ProfilUser):
    Pilihan = input("Pilih opsi (1-5): ")
    
    if Pilihan == '1':
        ProfilUser = profil(ProfilUser)
    elif Pilihan == '2':
        kalkulator()
    elif Pilihan == '3':
        daftar_informasi_kalori()
    elif Pilihan == '4':
        # Pastikan ProfilUser sudah ada
        if ProfilUser:
            # Ambil kebutuhan kalori harian
            KaloriHarian = kebutuhan_kalori_harian(
                ProfilUser['Jenis Kelamin'], 
                ProfilUser['Berat Badan'], 
                ProfilUser['Tinggi Badan'], 
                ProfilUser['Umur'], 
                ProfilUser['Skala Aktivitas'], 
                ProfilUser['Target']
            )
            
            # Input kategori menu
            # KaloriHarian = int(input("Masukkan kalori harian Anda: "))
            KategoriMenu = input("Pilih kategori menu (sarapan/makan siang/makan malam): ").lower()
            KategoriMenu = KategoriMenu.capitalize()  # Menyusun kategori menjadi format yang sesuai

            # Input tujuan (untuk menambah kalori harian sesuai target pengguna)
            tujuan = ProfilUser['Target']  # Misalnya 'naik', 'tetap', atau 'turun'

            # Panggil fungsi rekomendasi menu dengan 3 argumen yang diperlukan
            rekomendasi = rekomendasi_menu(KategoriMenu, KaloriHarian, tujuan)
            
            if rekomendasi:
                print("\n==== Rekomendasi Makanan ====")
                print(f"Kelompok: {rekomendasi['Kategori']}")
                print(f"Makanan Utama: {rekomendasi['Makanan Utama']}")
                print(f"Kalori Utama: {rekomendasi['Kalori Utama']}")
                print(f"Makanan Pilihan: {', '.join(rekomendasi['Makanan Pilihan'])}")
        else:
            print("Silahkan buat profil terlebih dahulu.")
    elif Pilihan == '5':
        print("=== Exit ===")
        return ProfilUser, True  # Menandakan bahwa pengguna memilih keluar
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    return ProfilUser, False

def main():
    ProfilUser  = {}
    while True:
        menuUtama()
        ProfilUser , Keluar = opsiMenu(ProfilUser)  # Menerima nilai `keluar` dari opsiMenu
        if Keluar:
            if input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
                break

main()