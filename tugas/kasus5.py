
Hari = input("Masukkan Hari: ")
Usia = int(input("Masukkan Usia: "))

if Hari in ["Sabtu", "Minggu"]:
    if Usia > 60:
        print("Tiket masuk: Rp 40.000")
    elif Usia < 12:
        print("Tiket masuk: Rp 30.000")
    else:
        print("Tiket masuk: Rp 50.000")
else:
    if Usia > 60:
        print("Tiket masuk: Rp 20.000")
    elif Usia < 12:
        print("Tiket masuk: Rp 15.000")
    else:
        print("Tiket masuk: Rp 25.000")