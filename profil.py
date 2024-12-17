# profil.py
from database import databaseKalori

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
    elif a == "Wanita":
        perempuan = (66.5 + (13.75 * b) + (5.003 * c) - (6.75 * d)) * e
        return perempuan

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