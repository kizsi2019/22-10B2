szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
szam_lista =[]
for szam in szamok:
    if szam %3 == 0 and szam %2 == 0:
        szam_lista.append(szam)
print(szam_lista)