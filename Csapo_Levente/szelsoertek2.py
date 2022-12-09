lista = []

szam = (input("Adj meg egy számot! "))
while szam <= "":
    lista.append(szam)
    szam = (input("Adj meg egy számot! "))
print(lista)
min = lista[0]
max = lista[0]
for elem in lista:
    if elem < min:
        min = elem
    if elem > max:
        max = elem
print("A lista legkisebb eleme: ", min)
print("A lista legnagyobb eleme: ", max)