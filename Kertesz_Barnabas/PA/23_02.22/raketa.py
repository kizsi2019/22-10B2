ido = int(input("Hány órás visszaszámlálást tervezünk? "))
tarolo = None
while tarolo <= ido:
    print("Visszaszámlálás:",ido)
    ido = ido - 1   
print("A rakéta a visszaszámlálást követően ennyi órával indult:", tarolo)