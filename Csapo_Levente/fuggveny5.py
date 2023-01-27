lista = []
szam = int(input("Adj meg egy pozitív számot! "))
while szam > 0:
    lista.append(szam)
    szam = int(input("Adj meg egy számot, ha befejeznéd akkor negatív számot írj be! "))
def min(lista):
    min = lista[0]
    for elem in lista:
        if elem < min:
            min = elem
    return min
def max(lista):
    max = lista[0]
    for elem in lista:
        if elem > max:
            max = elem
    return max
def osszegzo(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg
print(lista)
print("Lista legkisebb eleme:", min(lista))
print("Lista legnagyobb eleme:", max(lista))
print("A lista összege: ", osszegzo(lista))