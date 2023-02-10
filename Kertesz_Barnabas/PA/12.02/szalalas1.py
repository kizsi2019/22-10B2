import random
lista = []
for i in range(5):
    szam = random.randint(1, 10)
    lista.append(szam)
darab = 0
for elem in lista:
    if elem % 3 == 0:
        darab = darab + 1
print(lista)
print("Ennyi darab 3-mal oszható random szám van:", darab)
