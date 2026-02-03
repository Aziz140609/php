jenis_sampah = input("Masukan jenis sampah(Logam/Plastik/Kertas)").lower()

if jenis_sampah == "logam" :
    print("Sampah Masuk ke Tong Merah")
elif jenis_sampah == "kertas" :
    kondisi = input("Apakah Kondisi Sampah(Basah/Kotor/Bersih/Kering): ").lower()
    if kondisi == "basah" or kondisi == "kotor":
        print("Sampah Anda Masuk Ke Tong Kompos/Hancur")
    elif kondisi == "bersih" or kondisi == "kering":
        print("Sampah Anda Masuk ke Tong Biru(Daur ulang)")
elif jenis_sampah == "plastik":
    kondisi = input("Apakah Kondisi Sampah(Berminyak/Kotor/Bersih/Kering): ").lower()
    if kondisi == "berminyak" or kondisi == "kotor":
        print("Sampah Anda Masuk Ke Tong Abu-abu(Residu)")
    elif kondisi == "bersih" or kondisi == "kering":
        print("Sampah Anda Masuk ke Tong Kuning(Daur ulang)")
else:
    print("Alarm Eror: Objek Tidak Dikenal")

    