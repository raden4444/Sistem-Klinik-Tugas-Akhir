def tambah_rekam_medis(data_pasien):
    id_pasien = input("Masukkan ID pasien yang dicari = ").strip().upper().replace(" ", "")
    if id_pasien in data_pasien:
       diagnosa = input("Masukkan Diagnosa = ")
       tindakan = input("Masukkan Tindakan = ")
       resep = input("Masukkan Resep = ")

       rekam_medis_baru = {
        "diagnosa": diagnosa,
        "tindakan": tindakan,
        "resep": resep,
       }

       data_pasien[id_pasien]["Rekam_Medis"].append(rekam_medis_baru)
       print("Rekam medis berhasil ditambahkan")
       print(data_pasien)
    else:
        print("Pasien Tidak Ditemukan!")

def lihat_rekam_medis(data_pasien):
    id_pasien = input("Masukkan ID Pasien yang dicari = ").strip().upper().replace(" ","")
    if id_pasien in data_pasien:

        lihat_rekam = data_pasien[id_pasien]["Rekam_Medis"]
        if len(lihat_rekam) == 0:
          print("Belum ada rekam medis!")

        else:
            for item in lihat_rekam:
                print("=====Rekam Medis Pasien=====")
                print("Diagnosa", item["diagnosa"])
                print("Tindakan", item["tindakan"])
                print("Resep", item["resep"])
                
    else:
        print("Pasien Tidak ditemukan!")