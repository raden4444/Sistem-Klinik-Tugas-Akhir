id_cari = input("Masukkan ID pasien: ")
if id_cari in data_pasien:

    pasien = data_pasien[id_cari]

    print("===== DATA PASIEN =====")
    print("ID       :", id_cari)
    print("Nama     :", pasien["Nama"])
    print("Usia     :", pasien["Usia"])
    print("Keluhan  :", pasien["Keluhan"])

else:
    print("Pasien tidak ditemukan")