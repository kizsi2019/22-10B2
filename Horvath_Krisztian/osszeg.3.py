lista =[]
osszeg = 0
szam = int(input("adj meg egy számot -5 és 5 között!"))
while -5 <szam < 5:
    osszeg = osszeg + szam
    lista.append(szam)
    szam =int(input("adj meg egy számot -5 és 5 között!"))
print(lista)
print("az összegük: " , osszeg)