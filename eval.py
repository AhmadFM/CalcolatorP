def profil():
   profilUser = {
        "nama": input ("Masukkan nama: "),
        "umur": input ("Masukkan umur: "),
        "berat":input ("Masukkan berat (kg): "),
        "tinggi":input ("Masukkan tinggi (cm): ")
    }   
   return profilUser

totalKalori = 0
listMakanan = []

def kalkulator():
    global totalKalori
    
    databaseKalori = {
    "nasi" : 300,
    "ayam" : 100,
    "sayur": 60,
    "tempe": 80
    } 

    print("\n==== KALKULATOR KALORI ====")
    jumlahMakanan = int(input("Masukkan jumlah jenis makanan yang anda makan: "))

    for i in range (jumlahMakanan):
        namaMakanan = input("Masukkan nama makanan: ")
        listMakanan.append(namaMakanan)

        if namaMakanan in databaseKalori:
            totalKalori = totalKalori + databaseKalori[namaMakanan]

        else:
            print("Nama makanan belum terdaftar dalam database!")

jumlahAkhirKalori = 0 + totalKalori
print(f"Total kalori yang anda makan (dalam gram) {listMakanan}: ", jumlahAkhirKalori)  


def menu_utama ():
    print("\n=== Menu Utama ===")
    print("1. Profil")
    print("2. Hitung Total Kalori")
    print("3. Keluar")

menu_utama()

pilihan = int(input("Pilih opsi (1-3): "))

if pilihan == 1:
    profil()
elif pilihan == 2:
    kalkulator()
elif pilihan == 3:
    print("Keluar")
else:
    print("Pilihan tidak valid. Silakan coba lagi.")