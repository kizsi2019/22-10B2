import random

szam = random.randint(-5, 5)
print(f'A generált szám: {szam}')

if szam > 0:
    print("A szám pozitív")
if szam % 2 == 0:
    print("A szám osztható kettővel")