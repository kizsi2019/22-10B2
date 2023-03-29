class tizB:
    def __init__(self, fiuk, lanyok) :
        self.fiuk = fiuk
        self.lanyok = lanyok
    def info (self):
        print(f'A 10B-be {self.fiuk} fiú {self.lanyok} lány jár.')

tizb_01 = tizB(29, 2)
tizb_01.info()

with open('tizb.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A 10B-be {tizb_01.fiuk} fiú {tizb_01.lanyok} lány jár.')
 