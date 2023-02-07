import random
szamok = []
szam = 1
while szam <= 10:
    veletlenszam = random.randint(0, 50)
    if veletlenszam % 4 == 0:
        szamok.append(veletlenszam)
    szam = szam + 1
print(szamok)
print("A lista annyi elemből áll: ", len(szamok))