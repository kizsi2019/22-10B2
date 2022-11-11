import random

lista = []
talalat = False
index = 0
for i in range(5):
    veletlen_szam = random.randint(1, 7)
    lista.append(veletlen_szam)
szam = int(input("Adj egy kurva számot!"))
while index < len(lista) and not talalat:
    if lista[index] == szam:
        talalat = True
    index += 1

if talalat:
    print("Van")
else:
    print("Nincs")
