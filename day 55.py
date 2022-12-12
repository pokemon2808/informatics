print (" list bangun datar")
print ("1 = persegi ")
print ("2 = persegi panjang")
print ("3 = lingkaran ")

pilihan =int(input(" pilihan bangun datar"))

if ( 0 < pilihan < 4):
    if (pilihan ==1):
        print(" luas persegi adalah ")
        print(" luas = sisi x sisi ")
        sisi = float(input("sisi ="))
        hasil = (sisi **2)
        print(" luas persegi= %.2f cm2"% hasil)

    elif( pilihan ==2):
    print(" luas persegi panjang")
    print("luas = panjang x lebar ")
    panjang = float(input("panjang="))
    lebar = float(input("lebar"))
    hasil = (panjang+lebar)
elif( pilihan ==3):
    print(" luas lingkarang adalah")
    print(" luas = phi 22/7 * jari * jari")
    phi = float(input("jari"))
    if phi % 7 ==0:
        phi =22/7
    else:
        phi= 3.14
        luas = phi * phi **2
        print(" luas = %f cm2"%luas)
else:
    print(" pilihan tidak tersedia")

