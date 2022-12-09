lista = []
szam = input('Adj egy számot ha már nem szeretnél hozzá adni üss egy ENTER-t:')

while szam != '':
    lista.append(szam)
    szam = input('Adj egy számot ha már nem szeretnél hozzá adni üss egy ENTEr-T:')
print(lista)

print("A lista legnagyobb eleme:", max(lista))
print("A lista legkisebb eleme:", min(lista))

