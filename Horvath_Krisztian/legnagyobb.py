def keres_legnagyobb_elemet(lista):
    legnagyobb = lista[0]  # Kezdetben a legnagyobb elem a lista első eleme

    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem

    return legnagyobb

# Példa lista
lista = [12, 45, 67, 23, 9, 55]

# Legnagyobb elem megtalálása a függvény segítségével
legnagyobb_elem = keres_legnagyobb_elemet(lista)

# Eredmény kiíratása
print("A lista legnagyobb eleme:", legnagyobb_elem)
