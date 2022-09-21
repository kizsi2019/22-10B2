szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

szamlalo = 1
while szamlalo <= 5:
    print("Programozni jó!")
    szamlalo += 1

folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input("Mondjam mégegyszer? (i/n)")
    if valasz == "n":
        folytatja = False
print("Program vége")

szam = int(input("Adj meg egy számot 5 és 10 között!"))
while not 5 <= szam <= 10:
    szam = int(input("Nem jó, add meg mégegyszer 5 és 10 között!"))
print("Rendben!")

szo = input("Adj meg egy szót! Ha kilépnél a szó helyett üssél ENTER-t!")

szo = None
while szo !='':
    szo = input("Adj meg egy szót! Ha kilépnél a szó helyett!")
print("Program vége")