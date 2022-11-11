import random
talalat=None
index = 0
lista = []
for i in range(5):
    veletlen_szam = random.randint(1,7)
    lista.append(veletlen_szam)
szam = int(input("Adj meg egy számot!"))
while index < len(lista) and not talalat:
    if lista[index] == szam:
        index += 1
print(lista)
if talalat:
    print("Van egy a listában olyan szám")
else:
    print('Nincs a lsitában olyan szám')