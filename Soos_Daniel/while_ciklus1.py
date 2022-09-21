szam = 1
while szam <= 10:
    print(szam)
    szam = szam+1

    szamlalo = 1
    while szamlalo <= 5:
        print("Programozni jó")
        szamlalo += 1

        folytatja = True
        while folytatja:
            print(" Vidd ki a szemetet!")
            valasz = input(" Mondjam még egyszer? (i/n)")
            if valasz == "n":
                folytatja = False
                print("Program vége")

szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')

szo = None
while szo != '':
    szo = input('Adj meg egy szót4 Ha kilépnél a szó helyett üssél ENTERT-t ! ')
print('Program vége!')