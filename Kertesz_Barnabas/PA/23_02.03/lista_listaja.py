import random

tarolo = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(3):
    sza = random.randint(0, 25)
    lista1.append(sza)
tarolo.append(lista1)

for i in range(3):
    sza = random.randint(0, 25)
    lista2.append(sza)
tarolo.append(lista2)

for i in range(3):
    sza = random.randint(0, 25)
    lista3.append(sza)
tarolo.append(lista3)

for i in range(3):
    sza = random.randint(0, 25)
    lista4.append(sza)
tarolo.append(lista4)

print(tarolo)