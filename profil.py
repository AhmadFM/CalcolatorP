# profil.py

def tampilkanProfil(profilUser):
    print("\n=== Profil ===")
    print(f"Nama: {profilUser['Nama']}")
    print(f"Umur: {profilUser['Umur']} tahun")
    print(f"JenisKelamin: {profilUser['JenisKelamin']}")
    print(f"Berat: {profilUser['Berat']} kg")
    print(f"Tinggi: {profilUser['Tinggi']} cm")
    print(f"Skala Aktivitas Fisik: {profilUser['SkalaAktivitas']}")
    print(f"Target: {profilUser['Target']}")
    print("Kebutuhan Kalori Harian: ", kebutuhan_kalori_harian(profilUser['JenisKelamin'], 
                                                               profilUser['Berat'], 
                                                               profilUser['Tinggi'], 
                                                               profilUser['Umur'], 
                                                               profilUser['SkalaAktivitas'], 
                                                               profilUser['Target']))
   
def kebutuhan_kalori_harian(JK, BB, TB, Umur, Skala, Target):
    
    if JK == "pria":
        kebutuhan = 66.5 + (13.75 * BB) + (5.003 * TB) - (6.75 * Umur)
    elif JK == "wanita":
        kebutuhan = 655.1 + (9.563 * BB) + (1.850 * TB) - (4.676 * Umur)
    else:
        return "KAMI TIDAK MENERIMA LGBTQ+, KAMI HANYA MENERIMA PRIA DAN WANITA."
    
    if Skala == 1:
        kaloriDaily = kebutuhan * 1.2
    elif Skala == 2:
        kaloriDaily = kebutuhan * 1.375
    elif Skala == 3:
        kaloriDaily = kebutuhan * 1.55
    elif Skala == 4:
        kaloriDaily = kebutuhan * 1.725
    elif Skala == 5:
        kaloriDaily = kebutuhan * 1.9
    else:
        return "Skala aktivitas tidak valid. Harus antara 1-5."

    if Target.lower() == "turun":
        return round(kaloriDaily - 500, 2)
    elif Target.lower() == "naik":
        return round(kaloriDaily + 500, 2)
    elif Target.lower() == "tetap":
        return round(kaloriDaily,2)
    else:
        return "Error: GAUSAH NGADI NGADI CUMAN BISA 'TURUN', 'TETAP', DAN 'NAIK'."

def buat_profil():
    """Fungsi untuk membuat profil baru."""
    profilUser = {
        "Nama": input("Masukkan Nama: "),
        "JenisKelamin": input("Masukkan JenisKelamin (Pria/Wanita): ".lower()),
        "SkalaAktivitas": float(input("Masukkan Skala Aktivitas Fisik (1-5): ")),
        "Umur": float(input("Masukkan Umur: ")),
        "Berat": float(input("Masukkan Berat (kg): ")),
        "Tinggi": float(input("Masukkan Tinggi (cm): ")),
        "Target": str(input("Target Berat Badan (Turun/Tetap/Naik): ")).lower()
    }
    return profilUser

def edit_profil(profilUser):
    """Fungsi untuk mengedit profil yang sudah ada."""
    print("\n=== Profil Sekarang ===")
    tampilkanProfil(profilUser)

    # Meminta inputan untuk masing-masing atribut
    profilUser['Nama'] = input(f"Masukkan nama baru (atau tekan Enter untuk tetap '{profilUser['Nama']}'): ") or profilUser['Nama']
    profilUser['JenisKelamin'] = input(f"Masukkan JenisKelamin baru (atau tekan Enter untuk tetap '{profilUser['JenisKelamin']}'): ") or profilUser['JenisKelamin']
    profilUser['SkalaAktivitas'] = float(input(f"Masukkan skala aktivitas fisik baru (atau tekan Enter untuk tetap '{profilUser['SkalaAktivitas']}'): ") or profilUser['SkalaAktivitas'])
    profilUser['Umur'] = float(input(f"Masukkan Umur baru (atau tekan Enter untuk tetap '{profilUser['Umur']}'): ") or profilUser['Umur'])
    profilUser['Berat'] = float(input(f"Masukkan Berat baru (atau tekan Enter untuk tetap '{profilUser['Berat']}'): ") or profilUser['Berat'])
    profilUser['Tinggi'] = float(input(f"Masukkan Tinggi baru (atau tekan Enter untuk tetap '{profilUser['Tinggi']}'): ") or profilUser['Tinggi'])
    profilUser['Target'] = input(f"Masukkan Target baru (atau tekan Enter untuk tetap '{profilUser['Target']}'): ") or profilUser['Target']
    
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
                tampilkanProfil(profilUser)
            elif pilihan == '2':
                profilUser = edit_profil(profilUser)
            elif pilihan == '3':
                print(kebutuhan_kalori_harian(profilUser['JenisKelamin'], profilUser['Berat'], profilUser['Tinggi'], profilUser['Umur'], profilUser['SkalaAktivitas'], profilUser['Target']))
                
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser