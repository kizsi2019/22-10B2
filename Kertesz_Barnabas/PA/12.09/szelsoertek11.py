lista = []
szam = input('Adj egy számot ha már nem szeretnél hozzá adni üss egy ENTER-t:')

while szam != '':
    lista.append(szam)
    szam = input('Adj egy számot ha már nem szeretnél hozzá adni üss egy ENTEr-T:')
print(lista)

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam < max:
        max = szam

print("A lista legnagyobb eleme:", max)
print("A lista legkisebb eleme:", min)
