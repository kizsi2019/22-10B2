szam = int(input("Adj meg egy számot! "))
szam2 = int(input("Adj meg egy másik számot! "))
if szam > szam2:
    print(szam, "Nagyobb mint", szam2)
elif szam < szam2:
    print(szam2, "Nagyobb mint", szam)
else:
    print("A kettő szám egyenlő")