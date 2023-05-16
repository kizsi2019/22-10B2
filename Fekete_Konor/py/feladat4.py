import random
import time

tarolo= []

list1 = []
list2 = []
list3 = []
list4 = []

for i in range (3):
    szam = random.randint(0,25)
    list1.append(szam)
    time.sleep(0.5)
    list2.append(szam)
    time.sleep(0.5)
    list3.append(szam)
    time.sleep(0.5)
    list4.append(szam)


tarolo.append(list1)
tarolo.append(list2)
tarolo.append(list3)
tarolo.append(list4)

print(tarolo)