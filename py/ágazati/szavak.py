szo = input("Adjon meg egy számot : ")

szo2 = input("adjon meg még egy számot : ")



if len(szo) < len(szo2):
    print(" A hosszabb szó :" , szo2)
elif len(szo) > len(szo2):
    print(" A hosszabb szó :" , szo)
else:
    print(" A két szó egyenlö hosszu")