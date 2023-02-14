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
print(homersekletek[0])   # [11, 19, 17]
print(homersekletek[0][1])  # 19

for nap in homersekletek:
	      for meres in nap:
		        print(meres)
    # érték módosítása
homersekletek[0][1] = 22

# érték beszúrása
homersekletek[0].insert(0, 0)

# sor beszúrása
homersekletek.insert(1, [0, 0, 0])

# érték törlése, a pop() metódus visszatérési értéke a törölt érték
del homersekletek[0][0]
homersekletek[0].pop(0)

# sor törlése
del homersekletek[1]
homersekletek.pop(1)
print(homersekletek)