import random

gondolt_szam = random.randit (1, 5)
szam = int(input("ajd meg egy számot! "))

if gondolt_szam == szam:
    print("a két szám egyenlő")
elif gondolt_szam < szam:
    print("a gondolt szám a kisebb!")
else:
    print("a gondolt szám a nagyobb")