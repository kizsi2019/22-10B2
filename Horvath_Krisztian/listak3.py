nev_lista = []
nev = None
while nev !='':
    nev = input("adj meg egy 'a' betűvel kezdödő nevet! ")
    if nev != '' and nev[0] == 'a':
        nev_lista.append(nev)
print(nev_lista)