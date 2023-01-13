import random

szam = random.randint(-5,5)

print(f'a generált szám:{szam}')

if szam > 0:
    print("a szám pozitiv")
if szam % 2 == 0:
    print("aszám osztható kettövel")