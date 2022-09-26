szam = int(input('Adj meg egy számot'))


if szam % 2 == 0 and szam > 0:
    print(szam, 'pozitive and páros')
if szam % 2 == 1 and szam < 0:
    print('szám negative')