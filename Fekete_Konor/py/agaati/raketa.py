vszam = int(input(" hány órás visszaszámlálást tervezünk ?"))

folytatja = True
while folytatja:
      print('visszaszámlálás : ', vszam )
      valasz = input('fel kell függeszteni a visszaszámlálást? (i/n)')
      vszam = vszam - 1
      if valasz == 'n' :
          folytatja = False
          