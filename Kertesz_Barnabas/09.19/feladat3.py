szam = int(input("Adj meg egy számot " ))
if szam % 3 == 0:
    print("A szám osztható 3-mal")
if szam % 4 == 0:
    print("A szám osztható 4-el")
if (szam % 3 == 0) or (szam % 4 == 0):
    print("A szám osztható 3-mal és 4-gyel is")
## BEFEJEZNI ##