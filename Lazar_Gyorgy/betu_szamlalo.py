szo = 'Ismered ezt a számot?'
szamlalo = 0
for betu in szo:
    if betu == 'E' or betu == 'e':
       szamlalo = szamlalo + 1
print(f'A sztringben {szamlalo} db e/E betű van!')

if 'e' in szo:
    print('Van benne e betű')
else:
    print('Nincs benne e betű')