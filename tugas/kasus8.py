
element_penyerang = input("Masukan Element untuk menyarang(Api/Air/Daun):").lower()
element_lawan = input("Masukan Element Untuk Lawan(Api/Air/Daun): ").lower()
power_serangan = int(input("Masukan Power Serangan(angka): "))

if element_penyerang == "api":
    if element_lawan == "api":
        total_power = power_serangan
        print("SERANGAN BERHASIL,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "air":
        total_power = power_serangan * 0.5
        print("SERANGAN LEMAH,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "daun":
        total_power = power_serangan * 2
        print("SERANGAN CRITYCAL,MUSUH TERKENA DAMAGE: ", total_power)
    else:
        print("Element Tidak ada")
elif element_penyerang == "air":
    if element_lawan == "api":
        total_power = power_serangan * 2
        print("SERANGAN CRITYCAL,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "air":
        total_power = power_serangan
        print("SERANGAN BERHASIL,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "daun":
        total_power = power_serangan * 0.5
        print("SERANGAN LEMAH,MUSUH TERKENA DAMAGE: ", total_power)
    else:
        print("Element Tidak ada")
elif element_penyerang == "daun":
    if element_lawan == "api":
        total_power = power_serangan * 0.5
        print("SERANGAN LEMAH,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "air":
        total_power = power_serangan * 2
        print("SERANGAN CRITYCAL,MUSUH TERKENA DAMAGE: ", total_power)
    elif element_lawan == "daun":
        total_power = power_serangan
        print("SERANGAN BERHASIL,MUSUH TERKENA DAMAGE: ", total_power)
    else:
        print("Element Tidak ada")
else:
    print("ELEMENT YG KAMU PILIH TIDAK ADA!!!")
        
        
