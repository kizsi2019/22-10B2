bejutott = False
while not bejutott:
    nev = input('Add meg a felhasználónevedet')
    jelszo = input('Add meg a jelszavad')
    if nev == 'bori99' and jelszo == 'szivecske<3':
        print('Belépés engedélyezve')
        bejutott = True
    else:
        print('Belépés megtagadva')