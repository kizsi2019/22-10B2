lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index <len(lista) and not talalat:
    if lista[index] % 3 ==0:
        talalat = True
    index = index +1
if talalat:
    print("Van 3-al osztható szám!")
else:
    print("Nincs 3-al osztható szám!")