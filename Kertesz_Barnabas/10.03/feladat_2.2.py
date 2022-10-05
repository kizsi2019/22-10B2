nev_lista = []
nev = None
while nev !='':
    nev = input("Adj meg egy 'a' betűvel kezdődö nevet! ")
    if nev != '' and (nev[0] == 'a' or nev[0] == 'A'):
        nev_lista.append(nev)
print(nev_lista)
