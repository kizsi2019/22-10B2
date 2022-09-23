szam = int(input("Adj meg egy számot! "))

if szam % 3 == 0 and szam % 4 == 0:
    print("mindkettovel oszthato")
if szam % 3 == 0:
    print("3al oszthato")
if szam % 4 == 0:
    print("4el oszthato")
