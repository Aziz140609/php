
Pendidikan_terakhir = input("Masukkan pendidikan terakhir Anda: ")

if Pendidikan_terakhir != "S1" and Pendidikan_terakhir != "s1" and Pendidikan_terakhir != "D3" and Pendidikan_terakhir != "d3":
    print("Maaf, pendidikan tidak memenuhi kualifikasi")
    exit()
    
Pengalaman_kerja = int(input("Masukkan pengalaman kerja Anda (dalam tahun): "))

if Pendidikan_terakhir == "S1" or Pendidikan_terakhir == "s1":
    if Pengalaman_kerja >= 2:
        print("Diterima sebagai Manager")
    elif Pengalaman_kerja < 2:
        print("Diterima sebagai Staff")
elif Pendidikan_terakhir == "D3" or Pendidikan_terakhir == "d3":
    if Pengalaman_kerja >= 5:
        print("Diterima sebagai Manager")
    elif Pengalaman_kerja < 5:
        print("Maaf, pengalaman belum cukup untuk D3")