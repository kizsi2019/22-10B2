class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg

allatfajok = []       

for _ in range(3):
    fajnév = input("Add meg egy állatfaj nevét! ")
    tömeg = input("Hány kilogramm a tömege egy példánynak?")
    allatfaj = Állatfaj(fajnév, tömeg)
    allatfajok.append(Állatfaj)

legnehezebb_allat = allatfajok[0]

for allatfaj in allatfajok:
    print("A(z)" , fajnév , "tö" , tömeg , " kg" ,sep='')
    if allatfaj.tömeg > legnehezebb_allat.tömeg:
        legnehezebb_allat = allatfaj

celfajl = open('legnehezebb.txt' , 'w')
print("A(z)" , legnehezebb_allat.fajnev , "a lenehezebb " , file=celfajl)