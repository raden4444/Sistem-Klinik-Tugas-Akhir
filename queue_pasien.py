from collections import deque
from menu_pasien import data_pasien
antrian_prioritas = deque()
antrian_reguler = deque()

def tambah_antrian():
   id_pasien = input("Masukkan ID pasien yang ingin dicari = ")
   if id_pasien in data_pasien:
    print ("=====Menu Antrian=====")
    print ("1. Antrian Prioritas")
    print ("2. Antrian Reguler")
    print ("0. Kembali")
   
    pilihan_pasien = int(input("Pilih angka (0-2)"))
    
    if pilihan_pasien == 1:
      antrian_prioritas.append(id_pasien)
      print ("Pasien masuk dalam antrian Prioritas")
    elif pilihan_pasien == 2:
      antrian_.append(id_pasien)
      print ("Pasien masuk dalam antrian Reguler")
      
    

