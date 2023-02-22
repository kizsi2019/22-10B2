visszaszam= int(input("Hány órára tervezi a visszaszámlálást?"))
if visszaszam > 0:
    print("Visszaszámlálás:", visszaszam)
    for i in range(visszaszam):
        valasz = input("Fel kell függeszteni a visszaszámlálást (i/n)?")
        if valasz ==