import random
lista =[]
talalat = False
index = 0
for i in range(5):
    veletlen_szam = random.randint(1,7)
    lista.append(veletlen_szam)
szam = int(input("Adj meg egy számot!"))
while index< len(lista) and not talalat:
    if lista[index] == szam:
        talalat = True
    index += 1
    print(lista)
if talalat:
    print('Van a listában olyan szám')
else:
    print('Nincs a listában olyan szám')