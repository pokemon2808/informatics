#menggunakan
kalimat = " Universitas Sulawesi Barat "
print(kalimat.upper())
print(kalimat.lower())
print(kalimat.title())
print(kalimat.replace("Sulawesi","Jawa"))
print(kalimat.count("a"))
...

kota = (" wonomulyo", "pamboang","majene"," mamuju","mamuju tengah "," polewali mandar ")
print(kota[5])
print(kota[2:5])
...

for ulang in range(1,20):
    if ulang==11:
        break
    print(ulang)
...
kata = input(" masukkan nama ")


for baris in range(len(kata)):
    for kol in range(baris+1):
        print(kata[kol],end='')
    print()