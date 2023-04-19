indul= int(input("Hány órás visszaszámlálást tervezünk?"))
felfüggesztések = 0
for szam in range(indul, 0,-1):
    print("Visszaámlálás:", szam)
    valasz = input('Fel kell függeszteni a visszaszámlálást(i/n)?')
    if valasz == 'i':
        felfüggesztések +=1
print('A rakéta a visszaszámlálást követően ennyi órával indult:', indul+felfüggesztések5)
