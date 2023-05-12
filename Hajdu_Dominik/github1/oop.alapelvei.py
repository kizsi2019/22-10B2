class  diak:
    def __init__(self, nev, osztaly,):
        self.nev = nev
        self.osztaly = osztaly
    def info(self):
            print(f'Szia, {self.nev} vagyok, és a(z) {self.osztaly} osztályba járok.')
diak_01 = diak('Kiss Péter', '10.A')   
class  tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak
    def info(self):
            print(f'Szia, {self.nev} vagyok, a {self.szak}')
tanar_01 = tanar('Horváth Zita', 'biológia-kémia szakos tanár vagyok.')
class  tanar1:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak
    def info(self):
            print(f'Szia, {self.nev} vagyok, a {self.szak}')
tanar_00 = tanar1('Schmidt Emil', 'matematika szakos tanár vagyok.')
print(diak_01.info()) 
print(tanar_01.info())
print(tanar_00.info())
