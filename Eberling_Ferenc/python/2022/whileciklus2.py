folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input("Monjam még egyszer? (Y/N)")
    if valasz == "N":
        folytatja = False
print("program vége!")