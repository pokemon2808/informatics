# program python percabangan

Nama = str(input(" Maukkan Nama :"))
Gol = input("golongan kerja :")
jam = int(input("masukkan jam kerja :"))
print(" 1.SMA\n2. D1\n3 D3 \n4 S1")
golpen = input(" Masukkan pendidikan ")
gaji = int(3000000)

### mengihtung golongan jabatan

if Gol =="1":
    upah =0.05*gaji
elif Gol =="2":
    upah =0.10*gaji
elif Gol =="3":
    upah = 0.15*gaji
else:
    upah =0

if golpen =="SMA":
    tunpen =0.025*gaji
elif golpen =="D1":
    tunpen = 0.05*gaji

elif golpen =="D3":
    tunpen = 0.20*gaji
elif golpen =="S1":
    tunpen = 0.30*gaji
else:
    tunpen = 0

if jam > 8:
    lembur = jam-8
    hlembur = lembur* 3500
else:
    print("Tidak ada golongan pendidikan")

rumus = tunpen + upah + gaji + hlembur

print("\n")
print("==================================================")
print("")
print("\n")
print("==================================================")
print("Nama \t\t\t\t",Nama)
print("Golongan kerja \t\t\t",Gol)
print(" Jumlah jam kerja \t\t", jam)
print(" Pendidikan \t\t\t", golpen)
print(" Gaji pokok \t\t\t", gaji)
print(" Tunjangan jabatan \t\t\t", upah)
print(" Tunjangan pendidikan \t\t\t", tunpen)
print(" Honor lembur \t\t\t", hlembur)
print(" Total gaji dan tunjangan \t", rumus)




