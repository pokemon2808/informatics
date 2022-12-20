#program menghitung gaji karyawan

print(" menghitung gaji karyawan ")
print("========================================================")
print()

nama = input("nama karyawan :")
golongan = input("golongan :")
jam_kerja = int(input( " jumlah jam kerja "))

print()

if golongan == "A" :
    upah_per_jam = 20000
elif golongan == "B" :
    upah_per_jam = 25000
elif golongan == "C" :
    upah_per_jam = 30000
elif golongan == "D" :
    upah_per_jam = 35000

total_upah = jam_kerja * upah_per_jam

if ( jam_kerja - 24) > 0:
    total_upah = total_upah +(( jam_kerja - 48)*15000)

print(nama, "menerima gaji Rp.",total_upah,"per minggu")