import datetime


class Diak:
    def _init_(self, nev, osztaly, szuletesi_ev):
        self.nev=nev
        self.osztaly=osztaly
        self.szuletesi_ev=szuletesi_ev
    def eletkor(self):
        datetime.datetime.now().year - self.szuletesi_ev
    def info(self):
        print(f'Szia, {self.nev} vagyok, a {self.osztaly} osztályos tanuló vagyok, {self.eletkor} éves vagyok.')

diak_1 = Diak('Kiss Pétekia', '10.b', 2005)
diak_1.info()
