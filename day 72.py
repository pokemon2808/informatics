for i in range(1,17,2):
    print(" i = ",i)

    ...

bilangan = int(input(" masukkan bilangan :"))

if bilangan %2 == 0:
    print("%i adalah bilangan genap "%bilangan)
else:
    print("%i adalah bilangan ganjil"%bilangan)

    ...
# function
def luas_persegi():
    sisi=int(input(" masukkan sisi"))
    luas = sisi*sisi
    print("luas", luas)
luas_persegi()

...

angka = int(input(" masukkan angka :"))

if angka %2 ==0 :
    print("%i bilangan ganjil", angka)
else:
    print(" %i bilangan genap", angka)