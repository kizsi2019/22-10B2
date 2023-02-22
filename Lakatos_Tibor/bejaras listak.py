'''
Hőmérséklet értékek 7:00, 15:00, 23:00 órakor
'''
homersekletek = []

pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]

homersekletek.append(pentek)
homersekletek.append(szombat)
homersekletek.append(vasarnap)
homersekletek.append(hetfo)

print(homersekletek[0]) # [11, 19, 17]

for nap in homersekletek:
    for meres in nap:
        print(meres)
del homerekletek[0][0]
print(homersekletek)
homersekletek[0].pap(0)
print(homersekletek)
