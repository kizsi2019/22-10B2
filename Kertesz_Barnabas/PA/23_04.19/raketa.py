tarolo = []
ido = int(input("Hány órás visszaszámlálást tervezünk? "))
ido.append(tarolo)
while tarolo <= ido:
    print("Visszaszámlálás:",ido)
    ido = ido - 1   
    valasz = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    
print("A rakéta a visszaszámlálást követően ennyi órával indult:", tarolo)