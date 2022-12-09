lista = []

szam = int(input("Adj meg egy számot! "))
while szam <= "":
    lista.append(szam)
    szam = int(input("Adj meg egy számot! "))
print(lista)
min = lista[0]
max = lista[0]
for elem in lista:
    if elem < min and % 2==0:
        min = elem
    if elem > max:
        max = elem
print("A lista legkisebb eleme: ", min)
print("A lista legnagyobb eleme: ", max)