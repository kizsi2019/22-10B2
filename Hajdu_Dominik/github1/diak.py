import datetime

class  diak:
    nagyobb_ev =0
    kisebb_ev =0
    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        if szuletesi_ev > 18:
            type(self).nagyobb_ev += 1
        else:
            type(self).kisebb_ev += 1
    def szuletesi_ev(self):
        return datetime.datetime.now().year -self.szuletesi_ev

    def info(self):
            print(f'Szervusz, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.szuletesi_ev} éves vagyok.')
      
diak_01 = diak('Hajdú Dominik', '10.B', 17)

print(diak_01.info())
  