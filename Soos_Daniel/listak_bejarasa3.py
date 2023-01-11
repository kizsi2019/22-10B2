szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
szo_lista = []
for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        szo_lista.append(szo)
print(szo_lista)