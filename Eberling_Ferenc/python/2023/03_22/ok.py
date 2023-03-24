class Szemely():
    
    def __init__(self, nev):
        self.nev=nev
    
    def bemutatkozik(self):
        print(f'Szia, a nevem {self.xnev}', end='')


class Diak(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly=osztaly
    
    def bemutatkozik(self):
        super().bemutatkozik()
        print(f' és a(z) {self.osztaly} osztályba fárok.')



class Tanar(Szemely):
    
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok=szakok
    
    def bemutatkozik(self):
        super().bemutatkozik()
        print('','-'.join(self.szakok), 'szakos tanár vagyok')


diak01=Diak('Anyád Szeretője', '10.FU')
tanar01 = Tanar('Szia Uram', ['kenyér dagasztás', 'nő csábítás'])
tanar02=Tanar('Van egy szál cigid?', ['cigi csórás'])

print(diak01.nev, diak01.osztaly)
diak01.bemutatkozik()
tanar01.bemutatkozik()
tanar02.bemutatkozik()