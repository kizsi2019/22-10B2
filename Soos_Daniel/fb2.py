import random
lista = []
def nagyobb(lista):
    max = lista[0]
    for elem in lista:
        if elem > max:
            max = elem
    return max
szam = input("Adj meg egy számot")
while szam !="":
    lista.append(int(szam))
    szam = input("Adj meg egy számot")

print(lista)
print(nagyobb(lista))
