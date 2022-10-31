angka=["galung","banggae","tinambung","pangkep","pamboang","","mamasa","wonomulyo","majene"]
kotayangdicari = input("ketik kota yang anda cari :")

for i, namakota in enumerate (kota):
    if namakota.lower()== kotayangdicari.lower():
        print("kota yang cari ada di indeks", i)
    break
else:
    print("maaf, kota yang anda cari tidak ada dalam list")