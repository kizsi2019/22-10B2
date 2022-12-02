szoveg = input("Adj meg egy")
while szoveg != '':
    if szoveg[-1] == '.':
        print('Ez a mondat kijelentő')
    if szoveg[-1] == '?':
        print('Ez a mondat kérdő')
    if szoveg[-1] == '!':
        print('Ez a mondat felkiálltó')
else:
    print('Nem irtál mondat zárást!')
    