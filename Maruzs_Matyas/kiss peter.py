class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly
    def into(self):
        print(f'Szia, a nevem Kiss Péter, és a(z) 10.A osztályba járok.')

class Tanar:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly
    def into(self):
        print(f'Szia, a nevem Horváth Zita, biológia-kémia szakos tanár vagyok.')

diak_01 = Diak('Kiss Péter', '10')
tanar_01 = Tanar('Kiss Zsigmond', 'informatika')
tanar_02 = Tanar('Nagy József', 'testnevelés')

diak_01.info()
tanar_01.info()
tanar_02.info()