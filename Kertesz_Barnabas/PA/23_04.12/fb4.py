def atlag(list):
    osszeg = 0
    for szam in list:
        osszeg += szam
    return osszeg/len(list)

lista = [1,2,3,4,5,6,7,8,9]
print(atlag(lista))