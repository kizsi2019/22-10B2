def sikeres(pont):
    if pont >= 48:
        return True
    else:
        return False
    
nev = None

while nev !='':
    nev = input("add meg a vizsgázó nevét! ")
    if nev:
        pont = int(input(" add mg a pontszámot "))
        if  sikeres(pont):
            print(nev ,"sikeres vizsga")
        else:
            print(nev ,"sikeretelen vizsga")