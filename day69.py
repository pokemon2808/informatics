# sebuah toko belanja menyeediakan diskon jika total belanja diatas 100.000 maka akan mendapatkan diskon sebesar 10%
#ouput( hasilnya ) nya adalah
# input belanjanya
#10% dikali total belanja

bayar = 2000000
belanja =int(input(" masukkan total belanja anda : " ))

if belanja >=100000:
    total_bayar=150000
    diskon =(10%(belanja))
    total_bayar2 = belanja - bayar -diskon
    print("bayar ",total_bayar2)
    print( " dapat diskon")
elif belanja <=100000:
    total_bayar =150000
    diskon=(10%(belanja))
    total_bayar2 = belanja -bayar -diskon
    print("bayar",total_bayar2)
    print("dapat diskon")
else:
    print(" anda tidak dapat diskon")




