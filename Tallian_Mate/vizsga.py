def sikeres(pontszam):
    if pontszam >= 48:
        return True
    else:
        return False

név = None

while név !="":
    név = input('Add meg a vizsgázó nevét!')
    if név:
        pontszám = int(input('Add meg a pontszámát!'))
        if sikeres(pontszám):
            print(név, 'vizsgája sikeres.')
        else:
            print(név, 'Vizsgája sikertelen.')