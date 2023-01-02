# pwnggunaan  perulangan untuk  nama
kata = input(" masukkan nama ")


for baris in range(len(kata)):
    for kol in range(baris+1):
        print(kata[kol],end='')
    print()