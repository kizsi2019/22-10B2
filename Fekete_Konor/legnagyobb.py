def legnagyobb_elem(lista):
    if not lista:
        return None

    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem

    return legnagyobb

lista = [3, 7, 1, 9, 2, 5]
legnagyobb = legnagyobb_elem(lista)
print("A lista legnagyobb eleme:", legnagyobb)
