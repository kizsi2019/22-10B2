szam = int(input("adj meg egy számot! "))
szam2 = int(input("adj meg egy számot! "))
if szam > szam2:
    print(szam, "nagyobb mint", szam2)
elif szam < szam2:
    print(szam2, "nagyobb mint", szam)
else:
    print("a kettő szám egyenlő")