import random
lista = []
osszeg = 0
for i in range(5):
    veletlen_szam = random.randint(1, 10)
    if veletlen_szam % 2 == 0 :
        osszeg = osszeg + veletlen_szam
    lista.append(veletlen_szam)
print(lista)
print("az összeg: ", osszeg)

