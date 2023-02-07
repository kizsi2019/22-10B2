import random

tarolo = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(3):
    szam = random.randint(0,25)
    lista1.append(szam)
for i in range(3):
    szam = random.randint(0,25)
    lista2.append(szam)
for i in range(3):
    szam =random.randint(0,25)
    lista3.append(szam)
for i in range(3):
    szam = random.randint(0,25)
    lista4.append(szam)
tarolo.append(lista1)
tarolo.append(lista2)
tarolo.append(lista3)
tarolo.append(lista4)
print(tarolo)