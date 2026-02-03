siswa =[{ "nama":"andi", "umur":15, "kelas":"10A"},
        { "nama":"budi", "umur":16, "kelas":"10B"}]

#for di dalam list
for x in siswa :
    print(x["nama"])

print("-----")

#for di dalam jangkauwan tertentu
for s in range(9) :
    print(s)
    
print("-----")
    
#while (Digunakan jika kita tidak tahu berapa kali perulangan akan dilakukan)
i = 1
while i <= 5 :
    print(i)
    i += 1
    
print("-----")
    
#while dengan break biar berhenti saat kondisi tertentu tanpa menunggu kondisi while terpenuhi
j = 1
while j <= 10 :
    print(j)
    j += 1
    if j > 5 :
            break

print("-----")

#continue (meng skip kondisi yg di tentukan lalu lanjut ke perulangan berikutnya)
for k in range(11) :
    if k == 2:
        continue
    print(k)