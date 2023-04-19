def óraperc(percek):
    óra = percek//60
    perc = percek - óra *60
    return  str(óra) + 'óra' + str(perc)+ ' perc'

for _ in range(3):
    cím =input('Add meg egy film címét!')
    hossz = int(input('Hány perces a film?'))
    print('A(z)', cím,'című film',óraperc(hossz),'hosszú.')