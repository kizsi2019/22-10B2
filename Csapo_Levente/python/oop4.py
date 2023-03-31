class TizB:
    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany

tizB = TizB(29, 2)

with open('tizb.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A 10B-be {tizB.fiu} fiú, és {tizB.lany} lány jár.')