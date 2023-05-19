class Állatfaj:
    def __init__(self,fajnév,tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg


állatok = []
for _ in range(3):
    fajnév = input("adj meg egy állat nevét : ")
    tömeg = input("Hány kilogramm az tömege : ")
    állatfaj = állatfaj(fajnév , tömeg)
    állatfaj.append(állatfaj)

legnehezebb_állat = állatok[0]

for állafaj in állatok:
    print('a(z)' állatfaj.fajnév, 'tömeg', állafaj.tömeg,'kg', sep='')
    if állatfaj.tömeg > legnehezebb_állatok.tömeg:
        legnehezebb_állat = állatfaj

célfálj = open('legnehezebb.txt' 'w')
print('a(az)' , legnehezebb_állat.fajnév, " a legnehezebb ", file=célfálj)
célfálj.close()

