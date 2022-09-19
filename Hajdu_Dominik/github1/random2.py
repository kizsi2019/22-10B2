import random

szam = random.randint(1, 5)
szam = int(input('Adj meg egy számot'))
print(f'A generált szám: {szam}')  

if szam < 5:
    print('A szám pozitív.')
if szam % 2 == 0:
    print('A szám páros.')


  