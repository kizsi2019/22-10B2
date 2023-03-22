import datetime


class diak:
    def __init__(self, nev, osztaly, ev):
        self.nev = nev
        self.osztaly = osztaly
        self.ev = ev
    def eletkor(self):
        datetime.datetime.now().year - self.ev

    def info(self):
        print(f'Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.eletkor} éves vagyok.')


diak_1 = diak("Minta János", "10.B", 2006)
diak_1.info()

diak_2 = diak("Minta Zsófia", "10.D", 2002)
diak_2.info()
