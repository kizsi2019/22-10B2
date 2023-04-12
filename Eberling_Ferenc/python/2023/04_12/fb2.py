def nagy(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max

szam = input("Adj meg egy számot: ")
lista = []
while szam != '':
    lista.append(int(szam))
    szam = input('Adj meg egy számot: ')
print(lista)
print(nagy(lista))