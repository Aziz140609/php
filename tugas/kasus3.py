
Total_belanja = int(input("Masukkan total belanja anda: "))
Member = input("Apakah anda member (ya/tidak): ")

if Member == "ya":
    Pangkat = input("Masukkan pangkat anda (Gold/Silver): ")
    if Pangkat == "Gold":
        if Total_belanja > 500000:
            Diskon = int(Total_belanja * 0.2)
            print("Anda mendapatkan diskon sebesar: Rp", Diskon )
            Total = Total_belanja - Diskon
            print("Total yang harus dibayar setelah diskon: Rp", Total)
        elif Total_belanja <= 500000:
            Diskon = int(0.1 * Total_belanja)
            print("Anda mendapatkan diskon sebesar: Rp", Diskon)
            Total = Total_belanja - Diskon
            print("Total yang harus dibayar setelah diskon: Rp", Total)
    elif Pangkat == "Silver":
         if Total_belanja > 500000:
              Diskon = int(0.1 * Total_belanja)
              print("Anda mendapatkan diskon sebesar: Rp", Diskon)
              Total = Total_belanja - Diskon
              print("Total yang harus dibayar setelah diskon: Rp", Total)
         elif Total_belanja <= 500000:
                Diskon = int(0.05 * Total_belanja)
                print("Anda mendapatkan diskon sebesar: Rp", Diskon)
                Total = Total_belanja - Diskon
                print("Total yang harus dibayar setelah diskon: Rp", Total)
elif Member == "tidak":
    print("Maaf, anda tidak mendapatkan diskon karena bukan member.")  
    print("Total yang harus dibayar: Rp", Total_belanja)  