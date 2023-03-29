import datetime


class Diak:
    def def__init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev

    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesi_ev

    def info(self):
        print(f'Szia, {self.nev} vagyok, a {self.osztály} osztalyba jarok {self.eletkor()} éves vagyok.')


diak_1 = Diak ('Kiss Péter' , '10.B' , 2005)
diak_1.info()
