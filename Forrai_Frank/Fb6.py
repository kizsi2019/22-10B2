import random
def szamolo(list):
    min = list[0]
    max = list[0]
    for elem in list:
        if elem <min:
            min = elem
        if elem > max:
            max = elem
    return max - min

lista = [2, 4, 6, 8, 10]
lista = []
for i in range(10):
    szam = random.randit(0,20)
    lista.appened(szam)
    print(lista)
print ("a legnagyobb és a legkisebb elem különbség: ", szamolo(lista))