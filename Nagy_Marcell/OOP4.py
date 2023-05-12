class TizB:
    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany


tizB_01 =TizB(29,2)

with open('tizb.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A 10B-be {tizB_01.fiu} fiú, és {tizB_01.lany} lány jár')