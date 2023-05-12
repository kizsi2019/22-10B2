def atlag(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg/len(lista)

lista = [1,2,3,4,5,6,7,8,]
print(atlag(lista))
