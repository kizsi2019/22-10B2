def osszegzo(lista):
    osszeg = 0
    for szam in lista:
        osszeg = osszeg + szam
    return osszeg
lista = {1,3,5,7,9}
print(osszegzo(lista))
