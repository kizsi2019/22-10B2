lista = [12,5,4,8,9,11,10,12,6]
min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam
print('A legkisebb szam a listában:', min)
print('A legnagyobb szam a listában:', max)