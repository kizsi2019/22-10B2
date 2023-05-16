bejutott = False

while not bejutott:
    felhasználónév=input('Add meg a felhasználó nevét!')
    jelszó=input('Add meg a jelszót!')
    if felhasználónév=='bori99' and jelszó=='Szivecske<3':
        print('Belépés engedélyezve.')
        bejutott = True
    else:
        print('Belépés megtagadva.')