import datetime

class diak:
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
    def eletkor (self):
            return datetime.datetime.now().year - self.szuletesi_ev

    def info(self):
            print(f'Szia, {self.nev} vagyok, a {self.osztaly} osztalyba jarok, {self.eletkor()} eves vagyok.')


diak_1 = diak('Kiss Péter', '10.B', 2005)
diak_1.info()