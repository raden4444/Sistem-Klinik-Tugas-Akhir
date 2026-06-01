data_pasien = {}

def tambah_pasien():

    while True:
        id_pasien = (input("Masukkan ID Pasien = ")).strip().upper()
        if id_pasien == "":
           print("ID pasien tidak boleh kosong")
        elif id_pasien in data_pasien:
           print("ID pasien sudah digunakan!")
        else:
           break

    Nama = input("Masukkan Nama = ")
    
    while True:
        try:
            Usia = int(input("Masukkan Usia Pasien = "))
            break
        except ValueError:
            print("Usia harus berupa angka")
    

    Keluhan = input("Masukkan Keluhan = ")
    
    while True:
        tingkat_urgensi = input("Tingkat urgensi (rendah/tinggi )= ").strip().upper().replace(" ","")
        if tingkat_urgensi == "TINGGI" or tingkat_urgensi == "RENDAH":
            break
        else:
            print("Jawaban tidak valid!")
    
    data_pasien[id_pasien] = {
        "Nama": Nama,
        "Usia": Usia,
        "Keluhan": Keluhan,
        "Tingkat_Urgensi": tingkat_urgensi.capitalize(),
        "Rekam_Medis": []
    }

    print("Pasien berhasil ditambahkan")

def cari_pasien():
    cari = input("Masukkan ID pasien yang dicari = ").strip().upper().replace(" ", "")

    if cari in data_pasien:

        pasien = data_pasien[cari]

        print("===== DATA PASIEN =====")
        print("ID       :", cari)
        print("Nama     :", pasien["Nama"])
        print("Usia     :", pasien["Usia"])
        print("Keluhan  :", pasien["Keluhan"])
        print("Tingkat_Urgensi  :", pasien["Tingkat_Urgensi"])

    else:
        print("Pasien tidak ditemukan")

def hapus_pasien():
    
    print(data_pasien)
    id_hapus = (input("Masukkan id yang ingin dihapus : ")).strip().upper().replace(" ", "")

    if id_hapus in data_pasien:
      del data_pasien[id_hapus]
      print("Data berhasil dihapus")

    else:
        print("Pasien tidak ditemukan")

def update_pasien():
    id_update = input("Masukkan ID pasien yang ingin diubah = ").strip().upper().replace(" ", "")
    if id_update in data_pasien:
        pasien = data_pasien[id_update]
        print("===== DATA LAMA =====")
        print("Nama     :", pasien["Nama"])
        print("Usia     :", pasien["Usia"])
        print("Keluhan  :", pasien["Keluhan"])
       
        print("===== MASUKKAN DATA BARU =====")
        nama_baru = input("Masukkan Nama Baru = ")
        try:
            usia_baru = int(input("Masukkan Usia Baru = "))
        except ValueError:
            print("Usia harus angka")
            return
        keluhan_baru = input("Masukkan Keluhan Baru = ")

        pasien["Nama"] = nama_baru
        pasien["Usia"] = usia_baru
        pasien["Keluhan"] = keluhan_baru

        print("Data pasien berhasil diupdate")

        print("DEBUG DATA:")
        print(data_pasien)

    else:
        print("Pasien tidak ditemukan")  