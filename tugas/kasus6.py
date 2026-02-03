gaji_pokok = float(input("Masukkan gaji pokok Anda: "))

nikah = input("Apakah Anda sudah menikah? (ya/tidak): ").lower()
tunjangan_pasutri = 0
tunjangan_anak = 0
if nikah == "ya":
    tunjangan_pasutri = gaji_pokok * 0.1
    jumlah_anak = int(input("Masukkan jumlah anak(angka): "))
    if jumlah_anak == 2:
        tunjangan_anak = gaji_pokok * 0.05
    elif jumlah_anak > 1:
        tunjangan_anak = 0.1 * gaji_pokok
    else:
        print("anda tidak mendapatkan tunjangan anak")
else:
    tunjangan_pasutri = 0
    tunjangan_anak = 0


print("Anda mendapatkan tunjangan sebesar:Rp", tunjangan_anak + tunjangan_pasutri) 
total_gaji = gaji_pokok + tunjangan_pasutri + tunjangan_anak
print("Total gaji Anda adalah:Rp",int(total_gaji))