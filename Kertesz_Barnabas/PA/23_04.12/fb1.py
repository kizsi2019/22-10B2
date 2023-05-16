import random

def paros_e(lista):
    paros = []
    for elem in lista:
        if elem % 2 == 0:
            paros.append(elem)
    return paros

#lista = [1,2,3,4,5,6,7,8,9,10]
lista = [ ]
#for i in range(10):
    #szam = random.randint(0, 10)
    #lista.append(szam)
#print("A hozzáadás sikeres volt.")

szam = input("Adj meg egy számot ")
while szam !='':
    lista.append(int(szam))
    szam = input("Adj meg egy számot ")

print(paros_e(lista))
#print(lista)

