szoveg = input(" Adj meg egy mondatot!")
if szoveg[-1] == '.':
    print("Ez a mondat kijelentő!")
if szoveg[-1] == '?':
    print("Ez a mondat kérdő!")
if szoveg[-1] == '!':
    print("Ez a mondat felkiáltó/óhajtó!")
