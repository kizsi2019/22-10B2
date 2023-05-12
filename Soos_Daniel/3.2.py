class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg
állatfajok = []
for _ in range(3):
    fajnév = input('Add meg egy állatfaj nevét')
    tömeg = input('Hány kilogramm a tömege egy példánynak')
    állatfaj = Állatfaj(fajnév, tömeg)
    állatfajok.append(állatfaj)
legnehezbb_állat = állatfajok[0]
for állatfaj in állatfajok:
    print('A(z)', állatfaj.fajnév, 'tömege', állatfaj.tömeg,'kg', sep='')
    if állatfaj.tömeg > legnehezbb_állat.tömeg:
        legnehezbb_állat = állatfaj
célfájl = open('legnehezebb.txt', 'w')
print('A(z)',legnehezbb_állat.fajnév, 'a legnehezebb.', file=célfájl)
célfájl.close()