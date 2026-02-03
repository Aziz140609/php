siswa = [
    {"nama": "andi", "umur": 15, "kelas": "10 RPL 1"},
    {"nama": "budi", "umur": 16, "kelas": "10 RPL 2"},
    {"nama": "cici", "umur": 15, "kelas": "10 TKJ 1"},
    {"nama": "dina", "umur": 16, "kelas": "10 TKJ 2"},
    {"nama": "eko",  "umur": 15, "kelas": "10 MM 1"},
    {"nama": "fajar","umur": 16, "kelas": "10 MM 2"},
]

umur_siswa = int(input("Masukkan umur siswa yang dicari: "))

for s in siswa:
    if s["umur"] == umur_siswa:
        print(s["nama"])
