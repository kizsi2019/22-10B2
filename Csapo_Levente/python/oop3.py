import random

class Kor:
    def __init__(self, sugar, kozeppont=(0, 0)):
        self.kozeppont = kozeppont
        self.sugar = sugar

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar * 2 * 3.14

    def info(self):
        print(f'A(z) {self.sugar} egység sugarú, {self.kozeppont} középpontú kör területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység.')

korok = []
for _ in range(5):
    kor = Kor(random.randint(0, 10))
    korok.append(kor)

for kor in korok:
    kor.info()
    
korok[0].info()