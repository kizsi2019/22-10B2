darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        if darab_karakter == oszlop:
            print('0', end='')
        else:
            print('.', end='')
        oszlop = oszlop = + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
