
def nagyobb(list):
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max

lista = [ ]

szam = input("Adj meg egy számot ")
while szam !='':
    lista.append(int(szam))
    szam = input("Adj meg egy számot ")

print(nagyobb(lista))

