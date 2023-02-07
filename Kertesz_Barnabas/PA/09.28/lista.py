import time

honapok = ['január', 'február', 'március', 'április']

print(honapok)  # Adatot írja ki #
print(', '.join(honapok))  # Szövegként írja ki #
print(len(honapok))    # Hosszát írja ki #
print(honapok[0])
print(', '.join(honapok[1:3]))
print(', '.join(honapok[:3]))
print(', '.join(honapok[2:]))
print(honapok[-1])

print("Újrainditás kérlek várj!")
time.sleep(5)
print('')

szo = "Almafa"
print(szo[:3])

print("Újrainditás kérlek várj!")
time.sleep(5)
print('')
gyumolcsok = []

gyumolcs = None
while gyumolcs != '':
    gyumolcs = input("Adj meg egy gyümölcsöt! ")
    if gyumolcs != '':
        gyumolcsok.append(gyumolcs)
print(', '.join(gyumolcsok))
