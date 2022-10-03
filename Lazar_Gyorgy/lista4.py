nev_lista = []
szam = 1
nev = None
while nev !='':
    nev = input("Adj meg egy 'a' betűvel kezdődő nevet")
    if nev != '' and (nev[0] == 'a' or nev[0] == 'A'):
            nev_lista.append(nev)
print(nev_lista)