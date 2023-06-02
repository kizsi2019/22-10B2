def nagy(lista):
    legnagyobb = lista[0]  
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem

    return legnagyobb


szamok = [2, 544, 23, 867, 75, 75]
legnagy = nagy(szamok)

print("A lista legnyagyob eleme:", legnagy)