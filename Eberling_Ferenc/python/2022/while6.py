import random
szam = 1
db = 0
while szam <= 20:
    veletlenszam = random.randint(1, 12)
    if veletlenszam % 3 == 0:
        print(veletlenszam)
        db = db + 1
    szam = szam + 1
print("Ennyi szám osztható hárommal: ", db)