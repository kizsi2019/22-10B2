def ponert(szam):
    siker = None
    if szam > 48:
        siker = True
    else:
        siker = False
    return siker
nev = input('Add meg a vizsgázó nevét! ')
while nev != "" :
    szam = int(input("Add meg a pontszámát! "))
    if ponert(szam) == True:
        print(f'{nev} vizsgája sikeres.')
    else:
        print(f'{nev} vizsgája sikertelen.')
    nev = input('Add meg a vizsgázó nevét! ')