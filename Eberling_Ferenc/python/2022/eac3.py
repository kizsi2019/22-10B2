dbkarakter = 1
sor = 1
while sor <=5:
    oszlop = 1
    while oszlop <=5:
        if dbkarakter == 6-oszlop or dbkarakter == oszlop:
            print("0 ", end='')
        else:
            print('. ', end='')
        oszlop = oszlop + 1
    print("")
    dbkarakter = dbkarakter + 1
    sor = sor + 1
