import random

gondol_szam = random.randint(1, 5)
szam = int(input("Adj meg egy számot (1-5 között)"))
print(f' A gondolt szám: {gondolt_szam}')
if gondolt_szam == szam:
    print(" A gondolt szám egyenlő")
elif gondolt_szam < szam:
    print
