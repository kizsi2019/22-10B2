lista = [0]
szam = int(input("Adj meg egy számot!"))
while szam 0:
    lista.append(szam)
    szam = int(input("Adj meg egy számot!"))
def max(lista):
    max = lista [0]
    for item in lista:
        if item > max:
            max = item
    return max
print(lista)
print("A lista legkisebb eleme: ",  max(lista))