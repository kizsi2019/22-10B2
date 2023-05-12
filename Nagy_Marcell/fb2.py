import random
def max_kereso(list):
    max = lista[0]
    for szam in list:
        if szam > max:
            max = elem
    return max

# lista = [1,2,3,4,5,6,7,8,9,10]
lista = []
# for i in range(10):
# szam = random.randint(0,10)
# lista.append(szam)

szam = input("Adj meg egy számot!")
while szam != '':
    lista.append(int(szam))
    szam = input("Adj meg egy számot!")

print(lista)
print(legnagyobb_e(lista))