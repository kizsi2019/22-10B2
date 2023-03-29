class people ():
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly

    def info(self):
        print(f'Szia, a nevem {self.nev} , és a {self.osztaly} osztályba járok.')

diak_1 = people("Kiss Péter", "10.A")
diak_1.info()

class teacher ():
    def __init__(self,  tnev, szak):
        self.tnev = tnev
        self.szak = szak

    def info(self):
        print(f'Szia, a nevem {self.tnev} , {self.szak} szakos tanár vagyok.')

tanar_1 = teacher("Horváth Zita", "biológia-kémia")
tanar_1.info()

tanar_2 = teacher("Schmidt Emil", "matematika")
tanar_2.info()
