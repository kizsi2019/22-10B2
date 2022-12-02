nev_lista = []
nev = None
while nev !='':
    nev = input("Adj meg egy 'a' betűvel kezdődő nevet!")
    if nev != '' and nev[0] == 'a':
        nev_lista.append(nev)
print(nev_lista)