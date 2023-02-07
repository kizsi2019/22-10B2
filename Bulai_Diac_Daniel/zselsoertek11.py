lista = []
szam = int(input("adj meg egy számot"))
while szam !="":
    lista.append(szam)
    szam = int(input('adj meg egy számot '))
print(lista)
min = szam[0]
max = szam[0]
for elem in lista:
    if elem < min:
        min = elem
    if elem > max:
        max = elem
    print('A legkisebb szám a listában: ', min)
    print('A legnagyobb szám a listában: ', max)