bekert = int(input("adj meg egy páros számot"))
darab_karakter = 1
sor = 1
while sor <= bekert/2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('o ',end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
darab_karakter = bekert/2
sor = bekert
while sor > 0:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('o ',end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor - 1

