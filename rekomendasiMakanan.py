import pandas as pd

def rekomendasi_makanan(target, kalori_harian, kategori):
    data = pd.read_csv("database.csv")

    faktor = 0.9 if target == 'turun' else 1.1 if target == 'tetap' else 1.1

    limit_kalori = kalori_harian * faktor

    skala_kategori = {
        "sarapan" : 0.3,
        "makan siang" : 0.4,
        "makan malam " : 0.3
    }

    if kategori in skala_kategori:
        batas_kalori = limit_kalori * skala_kategori[kategori]
    else:
        print("kategori tidak valid")
        return None
    
    karbohidrat = data[data['Kelompok'] == 'Serelia']
    karbohidrat_rekomendasi = karbohidrat[karbohidrat['Kalori'] <= batas_kalori]

    sisa_kalori = batas_kalori - karbohidrat_rekomendasi['Kalori'].values[0]

    makanan_lain = data[data['Kalori'] <= sisa_kalori]

    menu_rekomendasi = {
        "Karbohidrat": karbohidrat_rekomendasi ['Nama Makanan'].values[0],
        "Makanan lain": makanan_lain ['Nama Makanan'].tolist()
    }

    return menu_rekomendasi