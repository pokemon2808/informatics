# program python list buku

list_buku = []
while True:
    print(" masukkan data buku ")
    judul = input("masukkan judul buku\t : ")
    penulis = input(" masukkan penulis\t : ")

    buku_baru = (judul,penulis)
    list_buku.append(buku_baru)

    print(list_buku)

    print("No. \t judul \t\t\t\t penulis ")
    for index,buku in enumerate (list_buku):
        print(f"{index}.\t\t{buku[0]}\t\t\t {buku[1]}")