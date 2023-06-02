def nagy(lista):
    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem
    return legnagyobb

szamok = [2, 544, 6, 267, 75]
legnagy = nagy(szamok)

print("A lista legnagyobb eleme:", legnagy)