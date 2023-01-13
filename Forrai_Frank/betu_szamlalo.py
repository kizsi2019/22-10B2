szo = 'Ismered ezt a számot?'
szamlalo = 0
for betu in szo:
    if betu == 'E' or betu == 'e':
        szamlalo = szamlalo + 1
print(f'sztingben{szamlalo} db e/E betű van!')
if 'x' in szo:
    print('nincs benne x betű"')
else:
    print('Nincs benne x betű')