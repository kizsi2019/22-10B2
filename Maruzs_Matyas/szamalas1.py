import random
list = []
for i in range(5):
    szam = random.randint(1, 18)
    list.append(szam)
darab = 0
for elem in list:
    if elem % 3 == 0:
        darab += 1
print(list)
print("Ennyi darab hárommal osztható szám van a listámban", darab)