jawab="ya"
hitung=2

while (jawab =="ya"):
    hitung +=2
    jawab= input("apakah anda akan mengulang?")
    if jawab=="tidak":
        break
print(f"total perulangan:{hitung}")
