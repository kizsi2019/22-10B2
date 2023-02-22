folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input("Mondjam mégegyszer? (I/N) ")
    if valasz == "N":
        folytatja = False
print("Program vége!")
