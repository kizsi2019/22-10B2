homersekletek = []
pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]  

homersekletek.append(pentek)
homersekletek.append(szombat)
homersekletek.append(vasarnap)
homersekletek.append(hetfo) 
print(homersekletek[0]) 
(homersekletek[0][1])
for nap in homersekletek:
	      for meres in nap:
		        print(meres)
del homersekletek[0][0]
print(homersekletek)
homersekletek[0].pop(0)
print(homersekletek)
del homersekletek[1]
print (homersekletek)