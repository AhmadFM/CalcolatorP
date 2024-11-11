###########################
##  CALCOLATOR PROJECT   ##
###########################

##  VARIABEL UNIVERSAL  ##


##  FUNCTION LIST   ##
def kalkulatorKalori():
    pass

##  MAIN PROGRAM    ##
def profil():
   profilUser = {
        "nama": input ("Masukkan nama: "),
        "umur": input ("Masukkan umur: "),
        "berat":input ("Masukkan berat (kg): "),
        "tinggi":input ("Masukkan tinggi (cm): ")
    }   
   return profilUser

def tampilkan_profil(profilUser):
    print("\n=== Profil ===")
    print(f"Nama: {profilUser['nama']}")
    print(f"Umur: {profilUser['umur']} tahun")
    print(f"Berat: {profilUser['berat']} kg")
    print(f"Tinggi: {profilUser['tinggi']} cm") 

def menu_utama ():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Kalori Harian")
    print("3. Keluar")


def opsi_menu(profilUser):
    pilihan = input("Pilih opsi (1-3): ")
    if pilihan == '1':
        if not profilUser :
            profilUser = profil()
        else: 
            tampilkan_profil(profilUser)
    elif pilihan == '2':
        print("Hitung Kalori Harian")   
    elif pilihan == '3':
        print("Keluar")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    return profilUser
    
def main():
    profilUser  = {}
    while True:
        menu_utama()
        profilUser  = opsi_menu(profilUser )
        if not profilUser  and input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
            break

main()
