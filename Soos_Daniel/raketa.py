indul = input('Hány órás a visszaszámlálást tervezünk?')
indul = int(indul)
,
felfüggesztések = 0
for szám in range(indul, 0, -1):
    print('Visszaszámlálás:',szám)
    válasz = input('Fel kell fügeszteni a visszaszálálást(i/n)?')
    if válasz == 'i':
        felfüggesztések += 1
print('A rakéta a visszaszámlálást követően ennyi órával indult:', indul + felfüggesztések)