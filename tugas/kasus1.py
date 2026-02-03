# Program untuk menentukan kelulusan berdasarkan kehadiran dan nilai ujian
Presenntase_kehadiran = int(input("Masukkan presentase kehadiran (dalam persen): "))
Nilai_ujian = int(input("Masukkan nilai ujian: "))

if Presenntase_kehadiran >= 75:
  if Nilai_ujian >= 85:
    print("Selamat, Anda lulus dengan predikat A")
  elif Nilai_ujian >= 70:
    print("Selamat, Anda lulus dengan predikat B")
  elif Nilai_ujian <= 70:
    print("Selamat, Anda lulus dengan predikat C")
if Presenntase_kehadiran <= 74:
    print("Maaf, Anda tidak lulus karena kehadiran kurang dari 75%")

