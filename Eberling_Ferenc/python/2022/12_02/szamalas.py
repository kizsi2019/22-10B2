import random
lista = []
for i in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)
darab = 0
for elem in lista:
    if elem % 3 == 0:
        darab+=1
print(lista)
print("Ennyi hárommal osztható szám van a listában: ", darab)