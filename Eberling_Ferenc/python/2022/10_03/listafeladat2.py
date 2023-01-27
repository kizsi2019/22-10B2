szolista = []
szo=None
while szo != '':
    szo = input("Adj meg 'a' betűvel kezdődő nevet! ")
    if szo != '' and szo[0] == 'a' or "A":
        szolista.append(szo)
print(szolista)