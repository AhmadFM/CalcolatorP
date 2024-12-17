# main.py
from profil import profil
from kalkulator import kalkulator
from informasi_kalori import daftarInformasiKalori

def menu_utama():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Total Kalori Makanan")
    print("3. Informasi Kalori Makanan")
    print("4. Keluar")

def opsi_menu(profilUser ):
    pilihan = input("Pilih opsi (1-4): ")
    if pilihan == '1':
        profilUser  = profil(profilUser)
    elif pilihan == '2':
        kalkulator()
    elif pilihan == '3':
        daftarInformasiKalori()
    elif pilihan == '4':
        print("=== Exit ===")
        return profilUser , True  # Menandakan bahwa pengguna memilih keluar
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser , False  # Menandakan bahwa pengguna tidak memilih keluar

def main():
    profilUser  = {}
    while True:
        menu_utama()
        profilUser , keluar = opsi_menu(profilUser )  # Menerima nilai `keluar` dari opsi_menu
        if keluar:
            if input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
                break

# MAIN PROGRAM
main()