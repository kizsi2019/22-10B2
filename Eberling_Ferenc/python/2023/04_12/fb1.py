import random
def paros_e(list):
    paros = []
    for elem in list:
        if elem % 2 == 0:
            paros.append(elem)
    return paros

#lista = [1, 5, 3, 4, 5 , 6, 7, 8, 9, 10]
lista = []
#for i in range(10):
    #szam=random.randint(0, 10)
    #lista.append(szam)
#print(lista)
#print(paros_e(lista))

szam = input("Adj meg egyszámot")
while szam !='':
    lista.append(int(szam))
    szam = input("Adj meg egy számot")

print(lista)
print(paros_e(lista))