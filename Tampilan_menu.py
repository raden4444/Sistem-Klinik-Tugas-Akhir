from menu_pasien import tambah_pasien, cari_pasien, hapus_pasien, update_pasien, tambah_rekam_medis, lihat_rekam_medis
while True:
   print ("======SISTEM MANAJEMEN KLINIK SEHAT BERSAMA======")
   print ("1. Menu Pasien")
     #print(1. Mendaftarkan Pasien baru)
     #print(2. Mengecek Data Pasien)
       #print (1. Hapus data)
       #print (2. Perbarui Data)
       #print (3. Riwayat rekam medis)
       #print (3. mencatat tindakan terkahir) 
          #berisi diagnosa, resep, tindakan.
   print ("2. Menu Antrian")
     #print("1. Jumlah Antrian sekarang")
   print("3. Panggil pasien berikutnya")
        #urutan 1. prioritas
        #urutan 2. reguler
   print ("4. Laporan Harian")
     #print("1. Jumlah pasien hari ini")
     #print("2. Riwayat pembayaran")
   print ("5. Batalkan tindakan terakhir (undo)")
   print ("0. Keluar")
   print ("Pilih dengan memasukan angka (0-5)")
   print("=================================================")
   

   pilihan = int(input("Masukkan Angka = "))
   if pilihan == 1:
      while True:
         print("=====Menu Pasien=====")
         print("1. Mendaftarkan Pasien baru")
         print("2. Mengecek Data Pasien")
         print("3. Ubah Data Pasien")
         print("4. Hapus Data Pasie n")
         print("5. Tambah Rekam Medis")
         print("6. Lihat Rekam Medis")
         print("0. Kembali")
         print("Pilih angka(0-6)")
         pilihan_pasien = int(input("Masukkan Angka = "))
         if pilihan_pasien == 1:
            tambah_pasien()
         elif pilihan_pasien == 2:
            cari_pasien()
         elif pilihan_pasien == 3:
            update_pasien()
         elif pilihan_pasien == 4:
            hapus_pasien()
         elif pilihan_pasien == 5:
            tambah_rekam_medis()
         elif pilihan_pasien == 6:
            lihat_rekam_medis()
         elif pilihan_pasien == 0:
            break
         else:
            print("Pilihan tidak valid!")
   elif pilihan == 2:
      while True:
         print ("=====Menu Antrian=====")
         print("1. Jumlah Antrian sekarang")
         print("2. Panggil pasien berikutnya")
         print("0. Kembali")
         pilihan_antrian = int(input("Masukkan Angka = "))
         if pilihan_antrian == 1:
            #cek jumlah antrian sekarang
            pass
         elif pilihan_antrian == 2:
            #panggil pasien berikutnya
            pass
         elif pilihan_antrian == 0:
            break
         else:
            print("Pilihan tidak valid!")
   elif pilihan == 3:
      while True:
         print ("=====Menu Pemanggil Pasien=====")
         print("1. Pasien Prioritas")
         print("2. Pasien Reguler")
         print("0. Kembali")
         pilih_pemanggil = int(input("Masukkan Angka = "))
         if pilih_pemanggil == 1:
            pass
            #pilih prioritas
         elif pilih_pemanggil == 2:
            pass
            #pilih reguler
         elif pilih_pemanggil == 0:
            break
         else:
            print("Pilihan tidak valid!")
         
   elif pilihan == 4:
      while True:
         print ("=====Menu Laporan Harian=====")
         print("1. Jumlah pasien hari ini")
         print("2. Riwayat pembayaran")
         print("0. Kembali")
         pilih_laporan = int(input("Masukkan Angka = "))
         if pilih_laporan == 1:
            pass
            #tampilkan jumlah pasien hari ini
         elif pilih_laporan == 2:
            pass
            #tampilkan riwayat pembayaran pasien
         elif pilih_laporan == 0:
            break
         else:
            print("Pilihan tidak valid!")
   elif pilihan == 0:
      print ("=====Program Selesai=====")
      break 
   else:
      print("Pilihan tidak valid!")



   
   