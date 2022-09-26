szam = int(input("Adj meg egy párosszámot! : "))
dbkar = 1
sor = 1

while sor <= szam :
    oszlop = 1
    while oszlop <= dbkar:
        print("0", end='')
        oszlop = oszlop + 1
    print('')
    dbkar = dbkar + 1
    sor = sor + 1
sor2 = szam
dbkar2 = szam 
oszlop2= szam
while sor2 >= szam :
    oszlop2 = szam
    while oszlop2 >= szam:
        print("0", end='')
        oszlop2 = oszlop2 - 1
    print('')
    dbkar2 = dbkar2 - 1
    sor2 = sor2 - 1