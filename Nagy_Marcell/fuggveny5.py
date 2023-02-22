lista = []
szam = int(input("Adj meg egy számot!"))
while szam > 0:
    lista.append(szam)
    szam = int(input("Adj meg egy szamot!"))
def min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
            min = item
    return min
def max(lista):
    max = lista[0]
    for item in lista:
        if item < max:
            max = item
    return max
def osszegzo(lista):
    osszeg = 0
    for item in lista:
    osszeg += item
    return osszeg
print(lista)
print("A lista legnagyobb eleme", max(lista))
print("A lista legkisebb eleme", min(lista))
print("A lista osszege: ", osszegzo(lista))
