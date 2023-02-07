szoveg = input("Adj meg egy mondatot! ")
if szoveg[-1] == '.':
    print("Ez a mondat kijelntő!")
elif szoveg[-1] == '?':
    print("Ez  a mondat kérdő mondat!")
elif szoveg[-1] == '!':
    print('Ez a modat felkiáltó/óhajtó!')
else:
    print("Nincs írás jel a mondat végén")