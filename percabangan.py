a = 8
b = 7

#percabangan menggunakan  if
if a > b:
    print("a lebih besar dari b")
    
if a < b:
    print("a lebih kecil dari b")
    
if a == b:
    print("a sama dengan b")
elif a != b:
    print("a tidak sama dengan b")
    
    

#percabangan menggunakan nested if

Jadwal = input("Masukan jadwal (Jadwal A/Jadwal B): ")
hari = input("Masukan hari: ")

if Jadwal == "Jadwal A":
    if a > b:
        print("Pada Jadwal A")
        if hari == "Senin"or hari == "Rabu" or hari == "Jumat":
            print("Maka akan nge GYMM :) ")
    else:
        print("Pada Jadwal B")
        if hari == "Selasa" or hari == "Kamis":
            print("Maka akan paski :(")
    


