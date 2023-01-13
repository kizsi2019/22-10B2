import random
list = []
for i in range(5):
    szam = random.randint(1, 10)
    list.append(szam)
darab = 0
for elem in list:
    if elem % 3 == 0:
        darab += 1
print(list)
print("ennyi darab hárommal ossztható szám van a listában: ", darab)
