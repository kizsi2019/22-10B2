szam = int(input(" Adj meg egy számot : "))

if szam % 3 == 0:
    print("oszható háromal !")
elif szam % 4 == 0:
    print("Ez a szám oszható négyel")

if szam % 3 == 0 and szam % 4 == 0:
    print(" Ez a szám osztható négyel és háromal is ")
elif szam % 3 != 0 and szam % 4 != 0:
    print ("Nem osztható se négyel se háromal ")
