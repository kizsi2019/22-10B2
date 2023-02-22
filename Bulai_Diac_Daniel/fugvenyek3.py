lista = []
szam = int(input("adj meg egy szamot"))
while szam > 0:
    lista.append(szam)
    szam = int(input("adj meg egy szamot"))
def min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
            min = item
    return min
def max(lista):
    max = lista[0]
    for item in lista:
        if item > max:
            max = item
    return max
def osszegzo(lista):
    osszeg = 0
    for item in lista:
        osszeg += item
    return max

print(lista)
print("a lista legnagyobb eleme: ", min(lista))
print("a lista legkisebb eleme: ", min(lista))
print("a lista összege: ", osszegzo(lista))
