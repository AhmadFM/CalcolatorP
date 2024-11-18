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
    "dada ayam goreng (dengan kulit)" : 216,
    "dada ayam goreng (tanpa kulit)" : 184,
    "bebek goreng" : 286,
    "ikan lele goreng" : 105,
    "bakso sapi" : 202,
    "chicken nugget" : 297,
    "telur rebus" : 68,
    "telur dadar" : 93,
    "telur ceplok" : 92,
    "tempe goreng" : 118,
    "tempe bacem" : 119,
    "tahu isi" : 124,
    "tahu" : 113,
    "sambel goreng kentang" : 107,
    "pepaya" : 39,
    "melon" : 34,
    "pisang" : 89,
    "buah pir" : 58,
    "nanas" : 48,
    "apel" : 72,
    "buah naga" : 51,
    "mangga" : 65,
    "anggur" : 69,
    "sayur" : 60,
    "daging sapi" : 288,
    "daging sapi panggang" : 267,
    "udang goreng" : 287,
    "ikan salmon" : 146,
    "bayam" : 40,
    "kacang almond" : 597,
    "yogurt (polos)" : 61,
    "susu" : 50, 
    "kacang kedelai" : 471,
    "daging kambing" : 109,
    "gulai kambing" : 125,
    "daging domba" : 266,
    "daging bebek" : 132,
    "ikan salmon" : 146,
    "cappucino" : 440,
    "mie instan": 137,
    "kacang tanah" : 567,
    "kacang rebus" : 318,
    "kacang panjang" : 59,
    "kerang hijau" : 171,
    "kerang" : 217,
    "keju" : 403
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
    jumlahMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    i = 0  # Counter untuk loop

    while i < jumlahMakanan:
        namaMakanan = input("Masukkan nama makanan (huruf kecil semua): ")

        if namaMakanan in databaseKalori:
            listMakanan.append(namaMakanan)
            totalKalori += databaseKalori[namaMakanan]
            i += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{namaMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")

    print(f"Total kalori yang Anda makan dari {listMakanan} adalah {totalKalori} kkal")

def opsi_menu(profilUser):
    pilihan = input("Pilih opsi (1-3): ")
    if pilihan == '1':
        if not profilUser:
            profilUser = profil()
        else: 
            tampilkan_profil(profilUser)
    elif pilihan == '2':
        kalkulator()   
    elif pilihan == '3':
        main()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser
    
def main():
    profilUser  = {}
    while True:
        menu_utama()
        profilUser  = opsi_menu(profilUser)
        if not profilUser and input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
            break
           
##  MAIN PROGRAM  ##

main()
