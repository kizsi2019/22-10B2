import datetime


class Diak:

    def __int__(self,nev,osztaly,szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
    def eletkor(self):
        return self.szuletesi_ev - datetime.datetime.now().year

    def info(self):
        print(f'Szia,{self.nev} vagyok, a {self.osztaly} osztályába járok, {self.szuletesi_ev} éves vagyok')

diak_1 = Diak('Kiss Péter', '10.B', 2005)
diak_1.info()