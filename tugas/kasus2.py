username = "Admin"  
pasword = "Rahasia"

input_username = input("Masukkan username: ")
input_pasword = input("Masukkan pasword: ")

if input_username == username:
    if input_pasword == pasword:
        print("Login Berhasil, Selamat datang", username)
    else:
        print("Pasword Salah")
else:
    print("Username Tidak Ditemukan")