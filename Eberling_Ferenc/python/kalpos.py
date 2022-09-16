import random

x = random.randint(1,100)
szovegkezd = "Indulhat a jatek? (Y/N)"
print(szovegkezd)
szovegkezd2 = "Gondoltam egy számra..."
szovegkezd3 = "Akkor minek nyitottad meg?"
unalmasv = "Probald ujra!"
kicsi = "A szam amire gondoltam kissebb.", unalmasv
nagyi = "Nagyobb a szám amiore gondoltam.", unalmasv
grat = "Gratulalok! Eltalaltad a gondolt szamot :)))))"
szamvalasz = input()
valasz1 = input()
while valasz1 == "N":
    if valasz1 == "Y":
        print(szovegkezd2)
    elif valasz1 == "N":
        print(szovegkezd3)
while x == szamvalasz:
    if x < szamvalasz:
            print(kicsi)
    elif x > szamvalasz:
            print(nagyi)
    elif x == szamvalasz:
            print()