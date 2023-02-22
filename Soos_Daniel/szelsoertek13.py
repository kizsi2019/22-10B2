lista = []
szam = int(input("Adj meg egy szamot!!!!"))
while szam != "":
    lista.append(szam)
    szam = int(input("Adj meg egy szamot!!!!"))
    print(lista)
min = lista[0]
max = lista[0]
for elem in lista:
    if elem < min:
        min = szam % 2 == 0
    if elem > max:
        max = szam % 2 == 0
print('A legkisebb szam a listában:', min)
print('A legnagyobb szam a listában:', max)