class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg =tömeg
        
fajlista = []
tomeglista = []
for i in range(3):
    faj = input("Add meg egy állatfaj nevét! ")
    fajlista.append(faj)
    tomeg = input('Hány kilogramm a tömege egy példánynak? ')
    tomeglista.append(tomeg)

print(tomeglista, fajlista)
    