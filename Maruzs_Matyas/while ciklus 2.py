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

szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')

szo = None
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss! ')

print('Program vége!')
