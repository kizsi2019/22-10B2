szo = input('Adj meg egy szót!  ')
szo2= input('Adj meg egy másik szót! ')
if len(szo) > len(szo2):
    print("A hosszabb szó:", szo)
if len(szo) < len(szo2):
    print("A hosszabb szó:", szo2)
if len(szo) == len(szo2):
    print("A két szó egyforma hosszú.")