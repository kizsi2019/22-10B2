szamlista = []
szam = input('Adj meg egy számot majd ha befejezted üss egy ENTER-t: ')
while szam != "" :
    szamlista.append(szam)
    if szam !="":
        szam = input('Adj meg egy számot majd ha befejezted üss egy ENTER-t: ')
print(szamlista)
print("A legkisebb szám a listában: ", min(szamlista))
print("A legnagyobb szám a listában: " , max(szamlista))