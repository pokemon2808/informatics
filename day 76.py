def menu():
    nama = input(' masukkan nama pegawai')
    gaji_pokok = int(input(" masukkan gaji pokok"))
    jam_kerja = int(input(" masukkan jumlah jam kerja ="))
    gaji_kotor =  gaji_pokok * jam_kerja
    if gaji_kotor >500000 :
        pajak = 5 / 100 * gaji_kotor
        gaji_kotor = gaji_pokok * jam_kerja
        total = gaji_pokok - pajak
    else:
        pajak =0
        total = gaji_pokok - pajak
    print("gaji kotor anda adalah :",gaji_kotor)
    print(" pajak anda adalah :", pajak)
    print(" gaji bersih anda adalah :",total)
    print(" pegawai atas nama ",nama,"mendapatkan gaji sebesar  ",gaji_pokok)

menu()