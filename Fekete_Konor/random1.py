import random
from traceback import print_tb

szam = random.randint(-5, 5)
print(f'A Generált szám : {szam}')

if szam > 0:
    print(" A pozitiv ")
if szam % 2 == 0:
    print("A szám osztható kettövel ")