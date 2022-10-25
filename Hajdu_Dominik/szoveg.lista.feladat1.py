szoveg = input("adj meg egy mondatot!")
if szoveg[-1] == '.':
    print('Ez a mondatt kijelentő')
if szoveg[-1] == '?':
    print('Ez a mondatt kérdő')
if szoveg[-1] == '!':
    print('Ez a mondatt felkiálltó')
else:
    print('nem irtál mondat zárást!')
    