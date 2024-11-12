###########################
##  CALCOLATOR PROJECT   ##
###########################

##  VARIABEL UNIVERSAL  ##
total_kalori = 0

listMakanan = []

databaseKalori = {#per100gr
    "nasi" : 175,                        
    "kentang" : 87,
    "singkong" : 160,
    "ubi jalar" : 86,
    "Dada ayam goreng (dengan kulit)" : 216,
    "Dada ayam goreng (tanpa kulit)" : 184,
    "Bebek goreng" : 286,
    "Ikan lele goreng" : 105,
    "Bakso sapi" : 202,
    "Chicken nugget" : 297,
    "Telur rebus" : 68,
    "Telur dadar" : 93,
    "Telur ceplok" : 92,
    "Tempe goreng" : 118,
    "Tempe bacem" : 119,
    "Tahu isi" : 124,
    "Tahu" : 113,
    "Sambel goreng kentang" : 107,
    "Pepaya" : 39,
    "Melon" : 34,
    "Pisang" : 89,
    "Buah pir" : 58,
    "Nanas" : 48,
    "Apel" : 72,
    "Buah naga" : 51,
    "Mangga" : 65,
    "Anggur" : 69,
    "Sayur" : 60,
    "Daging sapi" : 288,
    "Daging sapi panggang" : 267,
    "Udang goreng" : 287,
    "Ikan salmon" : 146,
    "Bayam" : 40,
    "Kacang almond" : 597,
    "Yogurt (polos)" : 61,
    "Susu" : 50, 
    "Kacang kedelai" : 471,
    "Daging kambing" : 109,
    "Gulai kambing" : 125,
    "Daging domba" : 266,
    "Daging bebek" : 132,
    "Ikan salmon" : 146,
    "Cappucino" : 440,
    "Mie instan": 137,
    "Kacang tanah" : 567,
    "Kacang rebus" : 318,
    "Kacang panjang" : 59,
    "Kerang hijau" : 171,
    "Kerang" : 217,
    "Keju" : 403
}

##   PROCEDURE LIST   ##
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
##  FUNCTION LIST   ##
def profil():
   profilUser = {
        "nama": input ("Masukkan nama: "),
        "umur": input ("Masukkan umur: "),
        "berat":input ("Masukkan berat (kg): "),
        "tinggi":input ("Masukkan tinggi (cm): ")
    }   
   return profilUser

def kalkulator():
    global totalKalori
    totalKalori = 0 
    listMakanan.clear()
   
    print("\n==== KALKULATOR KALORI ====")
    jumlahMakanan = int(input("Masukan jumlah jenis makanan yang anda makan: "))

    for i in range (jumlahMakanan):
        namaMakanan = input("masukan nama makanan: ")
        listMakanan.append(namaMakanan)

        if namaMakanan in databaseKalori:
            totalKalori += databaseKalori[namaMakanan]
        else:
            print("Nama makanan belum terdaftar dalam database!")

    print(f"Total kalori yang anda makan (dalam gram) dari {listMakanan}: {totalKalori}")

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
           
##  MAIN PROGRAM    ##
main()
