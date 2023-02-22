szam = int(input("Adj meg egy párosszámot! : "))
dbkar = 1
sor = 1

while sor <= szam/2 :
    oszlop = 1
    while oszlop <= dbkar:
        print("0 ", end='')
        oszlop = oszlop + 1
    print('')
    dbkar = dbkar + 1
    sor = sor + 1
sor2 = szam
dbkar = szam/2
while sor > 0 :
    oszlop = 1
    while oszlop <= dbkar:
        print('0 ', end='')
        oszlop = oszlop + 1
    print("")
    dbkar = dbkar - 1
    sor = sor - 1
