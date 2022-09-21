szam = int(input("Adj meg egy számot! "))

if szam % 3 == 0:
    print("3al oszthato")
elif szam % 4 == 0:
    print("4el oszthato")
elif szam % 3 == 0 or szam % 4 == 0:
    print("mindkettovel oszthato")