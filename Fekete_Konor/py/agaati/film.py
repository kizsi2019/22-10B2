def óraperc(percek):
    
    óra = percek // 60
    perc = percek - "óra " + str(perc) + 'perc'

for _ in range(3):
    cim = input('add meg egy film cimét ! ')
    hossz = int(input("hány perces a film "))
    print('A(z)' , cim ,'cimü filme' , óraperc(hossz) 'hosszú')