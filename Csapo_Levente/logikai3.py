szam = int(input("Adj meg egy számot! "))

if szam % 3 == 0 and szam % 4 == 0:
    print("mindkettovel oszthato")
elif szam % 3 == 0:
    print("3al oszthato")
elif szam % 4 == 0:
    print("4el oszthato")
else:
    print("Nem oszthato semmelyikkel!")