class Diak:
    def __init__(self,nev,osztaly)
        self.nev,osztaly
        self.nev = nev
        self.osztaly = osztaly

    def info(self):
        print(f'Szia, a neve, {self.nev}, és a(z) {self.osztaly} osztalyba.' )

    class Tanar:
        def __init__(self, nev, szak):
            self.nev = nev
            self.szak = szak
    def info(self):
        print(f'Szia, a nevem {self.nev}, és a(z) {self.szak} szakos tanár vagyok.')

diak_01 = Diak('Kiss Péter', '10A')
tanar_01 = Tanar('Kiraly Boss','Élettan')
tanar_02 = Tanar('Dévényi Majom', 'Informatika')


diak_01.info()
tanar_01.elet()
tanar_02.info()

