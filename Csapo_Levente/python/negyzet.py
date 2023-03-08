class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz * self.oldalhossz
    def info(self):
        print(f'A(z) {self.oldalhossz} oldalhosszúságú, négyzet területe = {self.terulet()}, és kerülete = {self.kerulet()} egység.')
negyzet01 = Negyzet(20)
print(negyzet01.kerulet())
print(negyzet01.terulet())
print(negyzet01.info())