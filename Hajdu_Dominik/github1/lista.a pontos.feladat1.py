import random

tarolo = []
list1 = []
list2 = []
list3 = []
list4 = []

for i in range(3):
    szam = random.randint(0,25)
    list1.append(szam)
for i in range(3):
    szam = random.randint(0,25)
    list2.append(szam)
for i in range(3):
    szam = random.randint(0,25)
    list3.append(szam)
for i in range(3):
    szam = random.randint(0,25)
    list4.append(szam)
tarolo.append(list1)
tarolo.append(list2)
tarolo.append(list3)
tarolo.append(list4)
print(tarolo)
print(list1)
print(list2)
print(list3)
print(list4)