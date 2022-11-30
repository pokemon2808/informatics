# program python blangan prima

def is_prima  (x):
    return True

def is_prime (x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(2))
print(is_prime(4))
print(is_prime(11))

def cari_bilangan_prima (awal, akhir):
    list_bilangan_prima = []

    for x in range(awal, akhir + 1):
        if is_prima(x):
            list_bilangan_prima.append(x)
    return list_bilangan_prima

print( cari_bilangan_prima(1, 40))
print( cari_bilangan_prima(100, 150))
print( cari_bilangan_prima(1050, 1100))