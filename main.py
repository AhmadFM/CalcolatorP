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

def menu_utama ():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Total Kalori Makanan")
    print("3. Informasi Kalori Makanan")
    print("4. Keluar")

def daftarInformasiKalori():

    print("\n==== INFORMASI KALORI MAKANAN ====")

    jumlahInformasiMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    j = 0  # Counter untuk loop

    tabel = []

    while j < jumlahInformasiMakanan:
        cariMakanan = input("Masukkan nama makanan: ")

        if cariMakanan in databaseKalori:
            tabel.append([cariMakanan, databaseKalori[cariMakanan]])
            print(tabel)
            # databaseKalori.get(cariMakanan)
            j += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{cariMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")
    tabelMakanan = tabulate(tabel, headers=["Nama Makanan", "Kalori"], tablefmt="grid")
    print(tabelMakanan)



def kalkulator():

    global totalKalori
    totalKalori = 0 
    listMakanan.clear()
   
    print("\n==== KALKULATOR KALORI ====")
    jumlahMakanan = int(input("Masukkan jumlah jenis makanan yang Anda makan: "))
    i = 0  # Counter untuk loop

    while i < jumlahMakanan:
        namaMakanan = input("Masukkan nama makanan: ")

        if namaMakanan in databaseKalori: 
            listMakanan.append(namaMakanan)
            totalKalori += databaseKalori[namaMakanan]
            i += 1  # Hanya meningkat jika makanan ditemukan di database
        else:
            print(f"{namaMakanan} belum terdaftar dalam database. Silakan masukkan nama makanan yang lain.")

    print(f"Total kalori yang Anda makan dari {listMakanan} adalah {totalKalori} kkal")

def tampilkan_profil(profilUser):
    print("\n=== Profil ===")
    print(f"Nama: {profilUser['nama']}")
    print(f"Umur: {profilUser['umur']} tahun")
    print(f"Jenis Kelamin: {profilUser['jenisKelamin']}")
    print(f"Berat: {profilUser['berat']} kg")
    print(f"Tinggi: {profilUser['tinggi']} cm")
    print(f"Skala Aktivitas Fisik: {profilUser['skalaAktivitas']}")
    print(f"Target: {profilUser['target']}")
    print("Kebutuhan Kalori Harian: ", kebutuhanKaloriHarian(profilUser['jenisKelamin'], profilUser['berat'], profilUser['tinggi'], profilUser['umur'], profilUser['skalaAktivitas']))
   
def kebutuhanKaloriHarian(a, b, c, d, e = float()):
    
    
    if a == "Pria":
        lakiLaki = (66.5 + (13.75 * b) + (5.003 * c) - (6.75 * d)) * e
        return lakiLaki

##  FUNCTION LIST   ##

def buat_profil():
    """Fungsi untuk membuat profil baru."""
    profilUser = {
        "nama": input("Masukkan nama: "),
        "jenisKelamin": input("Masukkan Jenis Kelamin (Pria/Wanita): "),
        "skalaAktivitas": float(input("Masukkan Skala Aktivitas Fisik (1-5): ")),
        "umur": float(input("Masukkan umur: ")),
        "berat": float(input("Masukkan berat (kg): ")),
        "tinggi": float(input("Masukkan tinggi (cm): ")),
        "target": input("Target Berat Badan (Turun/Tetap/Naik): ")
    }
    return profilUser

def edit_profil(profilUser):
    """Fungsi untuk mengedit profil yang sudah ada."""
    print("\n=== Profil Sekarang ===")
    tampilkan_profil(profilUser)

    # Meminta inputan untuk masing-masing atribut
    profilUser['nama'] = input(f"Masukkan nama baru (atau tekan Enter untuk tetap '{profilUser['nama']}'): ") or profilUser['nama']
    profilUser['jenisKelamin'] = input(f"Masukkan jenis kelamin baru (atau tekan Enter untuk tetap '{profilUser['jenisKelamin']}'): ") or profilUser['jenisKelamin']
    profilUser['skalaAktivitas'] = input(f"Masukkan skala aktivitas fisik baru (atau tekan Enter untuk tetap '{profilUser['skalaAktivitas']}'): ") or profilUser['skalaAktivitas']
    profilUser['umur'] = input(f"Masukkan umur baru (atau tekan Enter untuk tetap '{profilUser['umur']}'): ") or profilUser['umur']
    profilUser['berat'] = input(f"Masukkan berat baru (atau tekan Enter untuk tetap '{profilUser['berat']}'): ") or profilUser['berat']
    profilUser['tinggi'] = input(f"Masukkan tinggi baru (atau tekan Enter untuk tetap '{profilUser['tinggi']}'): ") or profilUser['tinggi']
    profilUser['target'] = input(f"Masukkan target baru (atau tekan Enter untuk tetap '{profilUser['target']}'): ") or profilUser['target']
    
    print("\nProfil berhasil diperbarui!")
    return profilUser

def profil(profilUser):
    """Fungsi untuk menampilkan atau mengedit profil yang sudah ada, atau membuat profil baru jika belum ada."""
    if not profilUser:
        print("\n=== Buat Profil Baru ===")
        profilUser = buat_profil()
    else:
        print("\n=== Menu Profil ===")
        print("1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Cek Kebutuhan Kalori")
        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == '1':
            tampilkan_profil(profilUser)
        elif pilihan == '2':
            profilUser = edit_profil(profilUser)
        elif pilihan == '3':
            print(kebutuhanKaloriHarian(profilUser['jenisKelamin'], profilUser['berat'], profilUser['tinggi'], profilUser['umur'], profilUser['skalaAktivitas']))
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser

## FUNCTION LIST ##
def opsi_menu(profilUser):
    pilihan = input("Pilih opsi (1-4): ")
    if pilihan == '1':
        profilUser = profil(profilUser)
    elif pilihan == '2':
        kalkulator()
    elif pilihan == '3':
        daftarInformasiKalori()
    elif pilihan == '4':
        print("=== Exit ===")
        return profilUser, True  # Menandakan bahwa pengguna memilih keluar
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser, False  # Menandakan bahwa pengguna tidak memilih keluar

def main():
    profilUser = {}
    while True:
        menu_utama()
        profilUser, keluar = opsi_menu(profilUser)  # Menerima nilai `keluar` dari opsi_menu
        if keluar:
            if input("Apakah Anda ingin keluar? (y/n): ").lower() == 'y':
                break
                

## MAIN PROGRAM ##
main()
