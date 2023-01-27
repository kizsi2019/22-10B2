import random
lista = []
talalat = False
index = 0
for i in range (5):
    veletle_szam = random.randint (1, 7)
    lista.append(veletle_szam)
szam = int(input("adj meg egy számot"))
while index < len(lista) and not talalat:
    if lista[index] == szam:
        talalat = True
    index += 1
print(lista)
if talalat:
    print('van a listában oylan szám')
else:
    print('nincs a listában olyan szám')