import os


sor = 1
szam_2 = int(input("Adj egy párosszámot: " ))
darab_karakter = 1
while sor <= szam_2/2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
darab_karakter = szam_2/2
sor = szam_2
while sor > 0:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop = oszlop + 1
    print("")
    darab_karakter = darab_karakter - 1
    sor = sor - 1