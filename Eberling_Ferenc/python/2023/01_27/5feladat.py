szam = int(input("Adj meg egy számot! "))
szamok = []
while szam>0:
    szamok.append(szam)
    szam = int(input("Adj meg egy számot! "))
def min(szamok):
    min=szamok[0]
    for item in szamok:
        if item < min:
            min = item
    return min
def max(szamok):
    max=[0]
    for item in szamok:
        if item > max:
            max = item
    return max
def osszeg(szamok):
    osszeg = 0
    for item in szamok:
        osszeg += item
    return osszeg

print("A lista legkisebb eleme: ", min(szamok))
print("A lista legnagyobb eleme: ", max(szamok))
print("Lista összege: ", osszeg(szamok))