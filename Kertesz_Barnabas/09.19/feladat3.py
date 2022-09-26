szam = int(input("Adj meg egy számot " ))
if szam % 3 == 0 or szam % 4 == 0:
    print("A szám osztható 3-mal és 4-gyel is")
elif szam % 3 == 0:
    print("A szám osztható 3-mal")
elif szam % 4 == 0:
    print("A szám osztható 4-el")
if not szam % 3 == 0 or szam % 4 == 0:
    print("Kapd be")
## BEFEJEZNI ##