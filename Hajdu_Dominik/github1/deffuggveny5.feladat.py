lista = []
szam = int(input("Adj meg egy számot"))
lista = [12, 3, 4, 7, 8, 22]
while szam > 0:
      lista.append(szam)
      szam= int(input('szoszi'))
def min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
          min = item
    return min
    print(lista)
print("A lista legkisebb eleme:", min(lista))



