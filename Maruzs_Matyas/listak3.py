nev_lista = []

nev = input("Adj meg egy 'a' betűvel kezdődő nevet!")
while nev !='':
    if nev[0] == 'a':
        nev_lista.append(nev)
    else:
        nev = input("Adj meg egy 'a' betűvel kezdődő nevet!")
print(nev_lista)