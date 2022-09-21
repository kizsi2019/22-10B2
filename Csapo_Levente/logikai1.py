szam = int(input("Adj meg egy számot! "))

if  szam % 2 == 0 and szam > 0:
    print(szam, "pozitiv es paros")
elif szam % 2 == 1 and szam < 0:
    print(szam, "negativ paratlan")