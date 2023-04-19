def atlag(list):
    osszeg = 0
    for elem in list:
        osszeg += elem
        return osszeg/len(list)

lista = [1,2,3,4,5,6,7,8,]
print(atlag(lista))