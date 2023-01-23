szo = 'Ismered ezt a számot'
szamlalo = 0
for betu in szo:
    if betu == 'e' or betu =='E':
        szamlalo = szamlalo + 1
print(f'A stringben {szamlalo} db e/E betű van!')
if 'x' in szo:
    print('Van benne X betű')
else:
    print('Nincs benne x betű')