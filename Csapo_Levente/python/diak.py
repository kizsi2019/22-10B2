import datetime

class Diak:
    nagy_ev = 0
    kiss_ev = 0
    def __init__(self, nev, osztaly, ev):
        self.nev = nev
        self.osztaly = osztaly
        self.ev = ev
        if ev > 18:
            type(self).nagy_ev += 1
        else:
            type(self).kiss_ev += 1
    def ev(self):
        return datetime.datetime.now().year - self.ev
    def info(self):
            print(f'Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.ev} éves vagyok.')
    
    @classmethod
    def flotta_db(cls):
        return cls.nagy_ev + cls.kiss_ev

    @staticmethod
    def flotta_info():
        return 'Üdvözölek az iskolába!'

diak_01 = Diak('Csapó Levente', '10.B', 17)

print(diak_01.info())