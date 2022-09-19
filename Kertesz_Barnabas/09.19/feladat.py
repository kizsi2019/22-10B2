import random

gondolt_szam = random.randint(1, 5)
szam = int(input("Adj egy számot: "))

if gondolt_szam == szam:
    print("A két szám egyenlő")
elif gondolt_szam < szam:
    print(" A gondolt szám kisebb!")
else:
    print("A gondolt szám nagyobb")
