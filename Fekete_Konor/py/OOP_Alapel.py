class Szemely:
    def _init_(self, nev,):
        self.nev = nev


class Diak:
    def _init_(self, nev, osztaly):
        super()._init_(nev)
        self.osztaly=osztaly

class Tanar(Szemely):
    def _init_( self, nev, szakok, ):
        super().__init__(nev)
        self.szakok=szakok

diak01 = Diak('Kiss Péter', '10.A')
tanar01 = Tanar( 'Horváth Zita', ['Biologia-Kémia'])
tanar02 = Tanar('Schamidt Emil', [' Matematika'])


print(diak01.nev)