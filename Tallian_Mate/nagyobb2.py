szam1 = int(input("Adj meg egy számot! " ))
szam2 = int(input("Adj meg egy másik számot! " ))
if szam1 > szam2:
    print(szam1, "Nagyobb mint", szam2)
elif szam1 < szam2:
    print(szam2, "Nagyobb mint", szam1)
else:
    print("A kettő szám egyenlő")