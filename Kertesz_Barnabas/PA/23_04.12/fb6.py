import random

def nagyobb(list):
    max = list[0]
    min = list[0]
    for elem in list:
        if elem < min:
            min = elem
        if elem > max:
            max = elem
    return max - min

lista = [ ]

for i in range (10):
   szam = random.randint(0, 20)
   lista.append(int(szam))
#szam = random.randint(0, 20)
#while szam !='':
    #lista.append(int(szam))
    #szam = input("Adj meg egy számot ")

print(nagyobb(lista))
print(lista)