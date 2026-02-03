#input biasa 
# A = input("Apalah bebas: ")
# print("Kamu memasukkan:", A)

#input dengan tipe data tertentu
# B = int(input("Masukkan angka bulat: "))
# print("Kamu memasukkan angka bulat:", B)
# C = float(input("Masukkan angka desimal: "))
# print("Kamu memasukkan angka desimal:", C)
# D = complex(input("Masukkan angka kompleks (contoh: 1+2j): "))
# print("Kamu memasukkan angka kompleks:", D)
# E = bool(int(input("Masukkan 0 untuk False, selain itu True: ")))
# print("Kamu memasukkan boolean:", E)
# F = str(input("Masukkan sebuah string: "))
# print("Kamu memasukkan string:", F)

#input untuk masukan list
siswa =[{"nama", "absen"}]

for i in range(3) :
    n = input("masuka nama siswa: ")
    o = int(input("masukan absen siswa: "))
    
    siswa.append({"nama": n, "absen": o})
    
print(siswa)