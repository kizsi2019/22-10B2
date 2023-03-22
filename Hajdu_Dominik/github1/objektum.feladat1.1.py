
class negyzet:
    def __init__(self, oldalhossza):
        self.oldalhossza = oldalhossza
    
    def terulet(self):
         return self.oldalhossza * self.oldalhossza

    def kerulet(self):
         return self.oldalhossza * 5

negyzet_01 = negyzet(10)
print(negyzet_01.terulet())
print(negyzet_01.kerulet())

