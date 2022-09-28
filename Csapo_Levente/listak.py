
honapok = ['január', 'február','március', 'április']

print(honapok)
print(', '.join(honapok))
print(len(honapok))
print(honapok[0])
print(honapok[3])
print(honapok[1:3])
print(honapok[:3])
print(honapok[2:])
print(honapok[-1])

szo = "almafa"
print(szo[:3])    


  # üres listát hoz létre
gyumolcsok = []
  
  # kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
      # hozzáfűzi a listahoz
      gyumolcsok.append(gyumolcs)
  
print(gyumolcsok)  
  
  