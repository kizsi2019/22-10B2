szam = int(input("Adj meg egy számot!"))
if szam % 3 == 0:
    print("A szám osztható hárommal!")
if szam % 4 == 0:
    print("A szám osztható néggyel")
if szam % 3 == 0 and szam % 4 == 0:
    print(" A szám hárommal és néggyel is osztható")