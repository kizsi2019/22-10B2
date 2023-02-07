import random
lista = []
osszeg = 0
for i in range(5):
    veletlen_sazm = random.randint(1,10)
    if veletlen_sazm % 2 == 0:
     osszeg = osszeg + veletlen_sazm
    lista.append(veletlen_sazm)
print(lista)
print("Az összeg: ",osszeg)