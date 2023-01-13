lista = []
szam = input('Adj egy számot! ')

while szam != '':
    lista.append(szam)
    szam = input('Adj egy számot! ')
print(lista)

print("A lista legnagyobb eleme:", max(lista))
print("A lista legkisebb eleme:", min(lista))