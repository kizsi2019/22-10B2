class Tenb:
    def __init__(self, fiu, lany):
        self.fiu = fiu
        self.lany = lany

tizB01 =Tenb(29,2)

with open('tizB.txt','w',encoding='utf-8') as celfajl:
    celfajl.write(f'a 10B-be {tizB01.fiu} fiu, és {tizB01.lany} lány jár')
