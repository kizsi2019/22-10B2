szam = 1
  while szam <= 10:
    print(szam)
    szam = szam + 1

     szamlalo = 1
  while szamlalo <= 5:
      print("Programozni jó!")
      szamlalo = szamlalo + 1

folytatja = True
while folytatja:
    print("vidd ki a szemetet!")
    valasz = input("mondjam mégegyszer? (i/n)")
    if valasz == "n":
        folytatja = False
print("program vége")

szam = int(input("adj meg egy számot 5 és 10 között!"))
while not 5 <= szam <= 10:
    szam =int(input("nem jó, add meg mégegyszer 5 és 10 között"))
print rendben

szo = input("adj meg egy szót! ha kiléptél szó helyet üssél entert")

szo = none
while szo !='':
   szo = input("adj meg egy szót! ha kiléptél szó helyet üssél entert")
print ("program vége")