def sikeresel(pontsz):
    if pontsz <= 48:
        return True
    else:
        return  False
pontsz = []   
 
nev = None
while nev != '':
    nev = input("Add meg a vizsgázó nevét!")
    if nev:
        pontsz = int(input("Add meg a pontszámát! "))
        if sikeresel(pontsz):
            print( nev , "vizsgája sikeres.")
        else:
            print(nev ,"vizsgaja sikertelen.")