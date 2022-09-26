darab_karakter = 1
sor = 1
bekert = int(input("Adj meg egy számot!"))
while sor <= bekert/2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0 ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
darab_karakter = bekert/2
while sor > 0:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor - 1
