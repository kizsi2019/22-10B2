class Diak:
    def __init__(self, nev , osztaly,):
        self.nev = nev
        self.osztaly = osztaly
    def info(self):
        print(f'szia a nevem {self.nev}és a {self.osztaly}ba járok')

class Tanar:
    def __init__(self, nev , szak,):
        self.nev = nev
        self.szak = szak
    def info(self):
        print(f'szia a nevem {self.nev}és {self.szak}os vagyok')

diak01 = Diak('Kiss Péter', '10.A')
tanar01 = Tanar( 'Horváth Zita', 'Biologia-Kémia')
tanar02 = Tanar('Schamidt Emil', ' Matematika')

diak01.info()
tanar01.info()
tanar02.info()
