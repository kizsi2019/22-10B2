<<<<<<< HEAD
import time

darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        if darab_karakter == oszlop:
            print('0 ', end='')
        else:
            print('. ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

time.sleep(3)
print("Újrainditás!")

darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        if darab_karakter == 6-oszlop or darab_karakter == oszlop:
            print('0 ', end='')
        else:
            print('. ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
=======
import time

darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        if darab_karakter == oszlop:
            print('0 ', end='')
        else:
            print('. ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

time.sleep(3)
print("Újrainditás!")

darab_karakter = 1
sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        if darab_karakter == 6-oszlop or darab_karakter == oszlop:
            print('0 ', end='')
        else:
            print('. ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
>>>>>>> eae544bf4b2db6f18dc6b89d92cf907ffeba29e5
