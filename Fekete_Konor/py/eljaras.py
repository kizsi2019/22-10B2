
def sikeres(pont):
    if pont > 48:
     
        return True
    else:
        
        return False
nev = None
while nev != '':
    nev = input("adj meg egy nevet : ")
    if nev :
        pont = int(input("add meg a elért pontszámot :"))
    if sikeres(pont):
         print( nev,"sikeres vizsgát tett")
    else:
        print(nev,"Sikertelen vigyát tett")

