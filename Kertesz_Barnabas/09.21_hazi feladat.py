szam = int(input(" Adj meg egy számot kérlek szépen:" ))

if szam % 3 == 0 and szam % 4 == 0:
    print("A szám háromal illetve négyel is osztható")
elif szam % 3 == 0:
    print("Oszható háromal az általad megadott szám")
elif szam % 4 == 0:
    print("Osztható négyel az általad megadott szám")
else:
    print ("Ez a szám nem osztató se négyel , se háromal")

## Frissitve 2022.09.23 10:55
