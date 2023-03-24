class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def terulet(self):
        return self.oldalhossz * self.oldalhossz

    def kerulet(self):
        return self.oldalhossz * 4

negyzet_01 = Negyzet(10)
print(negyzet_01.terulet())
print(negyzet_01.kerulet())