#program python Kasir

pilihan="ya"
while pilihan=="ya":
    print("""
    ==================================
    Nightcore Cafe
    List menu Minuman kopi
    
    ==================================
    A. ES Kopi susu   : Rp 15.000
    B. ES Kopi coklat : Rp 20.000
    C. ES Kopi Hitam  : Rp 15.000
    D. Pop ICE        : Rp 10.000
    ==================================
    """)
    pesan=str(input("masukkan list abjad menu kopi   ="))
    jumlah_pesan =int(input("masukkan jumlah pesanan ="))
    if pesan =="A":
        list_nama ="ES kopi susu"
        harga =(11000*jumlah_pesan)
        ppn =int(harga *0.1)
        if jumlah_pesan >= 5:
            diskon =int(harga * 0.2)
            total_harga = int(harga-diskon+ppn)
        else:
            diskon =(0)
            total_harga =int(harga+ppn)
    elif pesan =="B":
        list_nama = " Es kopi coklat "
        harga =(20000*jumlah_pesan)
        ppn = int(harga *0.1)
        if jumlah_pesan >=5:
            diskon = int(harga * 0.2)
            total_harga = int(harga-diskon+ppn)
        else:
            diskon =(0)
            total_harga = int(harga+ppn)
    elif pesan == "C":
        list_nama = "Es kopi hitam"
        harga = int(15000 * jumlah_pesan)
        ppn = int(harga * 0.1)
        diskon = 0
        total_harga = int(harga+ppn)
    elif pesan == "D":
        list_nama = "Pop ICE"
        harga = int(10000 * jumlah_pesan)
        ppn = int(harga * 0.1)
        diskon =0
        total_harga = int(harga+ppn)
    else:
        list_nama = "-"
        harga     = "-"
        ppn       = "-"
        diskon    = "-"
        total_harga = "-"
        pilihan = input("menu tidak tersedia, silahkan masukkan abjad menu ya/tidak = ")

    print("--------------------------")
    print("Nightcore Cafe")
    print("--------------------------")
    print("menu :",list_nama)
    print("jumlah pesan", jumlah_pesan)
    print("harga", harga)
    print("diskon :",diskon)
    print("ppn :", ppn)
    print("--------------------------")
    print("jumlah bayar :", total_harga)
    print("--------------------------")
    pilihan =input("apakah anda ingin order kembali  ya/tidak =")



