# profil.py

profilUser = {}
Biodata = ("Nama", "Umur", "Jenis Kelamin", "Berat Badan", "Tinggi Badan", "Skala Aktivitas", "Target")

def cetak(profilUser):
    for i in Biodata:
        print(i, ': ', profilUser.get(i))

def tampilkanProfil(profilUser):
    print("\n=== Profil ===")
    cetak(profilUser)
   
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
    profilUser = {}
    for i in Biodata:
        while True:
            try:
                if i == 'Nama':
                    profilUser[i] = str(input(f"{str(i)} : "))

                elif i == 'Jenis Kelamin':
                    pilihan = ['pria', 'wanita']
                    profilUser[i] = str(input(f"{str(i)} : ")).lower()
                    if profilUser[i] not in pilihan:
                        raise Exception("Hanya Menerima pria/wanita")
                    
                elif i == 'Target':
                    pilihan = ['naik', 'tetap', 'turun']
                    profilUser[i] = str(input(f"{str(i)} (Naik/Tetap/Turun) : ").lower())
                    if profilUser[i] not in pilihan:
                        raise Exception("Target Tersedia Naik/Tetap/Turun")
                    
                elif i == 'Skala Aktivitas':
                    profilUser[i] = float(input(f"{str(i)} (1 - 5) : "))
                    if not (1 <= profilUser[i] <= 5):
                        raise Exception("Silahkan Pilih Angka yang Sesuai (1 - 5)")
                    
                else:
                    profilUser[i] = float(input(f"{str(i)} : "))

            except ValueError:
                print("Invalid Input: Silahkan Masukan Data yang Sesuai")
            except Exception as e:
                print(f"Invalid input: {e}")
            else:
                break
    return profilUser

def edit_profil(profilUser):
    """Fungsi untuk mengedit profil yang sudah ada."""   
    print("\n=== Profil Sekarang ===")
    cetak(profilUser)

    print("\n=== Edit Profil ===")    
    for i in Biodata:
        while True:
            try:
                DataBaru = input(f"{i} : ").lower()
                if not DataBaru:
                    break

                if i == 'Nama':
                    profilUser[i] = str(DataBaru)

                elif i == 'Jenis Kelamin':
                    pilihan = ['pria', 'wanita']
                    if str(DataBaru).lower() not in pilihan:
                        raise Exception("Hanya Menerima pria/wanita")
                    profilUser[i] = str(DataBaru)
                    
                elif i == 'Target':
                    pilihan = ['naik', 'tetap', 'turun']
                    if str(DataBaru).lower() not in pilihan:
                        raise Exception("Target Tersedia Naik/Tetap/Turun")
                    profilUser[i] = str(DataBaru)
                    
                elif i == 'Skala Aktivitas':
                    if not (1 <= int(DataBaru) <= 5):
                        raise Exception("Silahkan Pilih Angka yang Sesuai (1 - 5)")
                    profilUser[i] = int(DataBaru) 

                else:
                    profilUser[i] = int(DataBaru)

            except ValueError:
                print("Invalid Input: Silahkan Masukan Data yang Sesuai")
            except Exception as e:
                print(f"Invalid input: {e}")
            else:
                break
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
                print("Kebutuhan Harian Anda: ",kebutuhan_kalori_harian(profilUser['Jenis Kelamin'], profilUser['Berat Badan'], profilUser['Tinggi Badan'], profilUser['Umur'], profilUser['Skala Aktivitas'], profilUser['Target']), "kkal")
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    return profilUser