lista = []
szam = int(input("Adj meg egy számot!"))
while szam < 0:
    lista.append(szam)
    szam = int(input("Adj meg egy számot!"))
def min(lista):
    min = lista[0]
    for item in lista:
         min = item
    return min
def max(lista):
    max = lista[0]
    for item in lista:
         max = item
    return max
def osszegzo(lista):
    osszeg =0
    for item in lista:
        osszeg += item
    return max
print("A lista legnagyobb eleme: ", max(lista))
print("a lista legkisebb eleme: ", min (lista))
print("A lista összege:",  osszegzo(lista))




