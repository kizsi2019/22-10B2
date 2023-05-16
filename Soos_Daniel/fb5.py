import random
def szamlolo(lista):
    min = lista[0]
    max = lista[0]
    for elem in lista:
        if elem < min:
            min = elem
        if elem > max:
            max = elem
    return max - min
#lista = [2, 4, 6, 8, 10]
lista = []
for i in range(10):
    szam = random.randint(0,20)
    lista.append(szam)
print(lista)
print("A legnagyobb és a legkissebb elem különbsége:" , szamlolo(lista))