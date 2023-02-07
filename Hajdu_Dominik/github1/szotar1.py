
polc = []

polc.append({
        'szerzo': 'William Golding',
        'cim': 'A legyek ura'
    })

polc.append({
        'szerzo': 'Ottlik Géza',
        'cim': 'Iskola a határon'
    })

print(polc)  

# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  
  

reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

    # metszet
print(reggeli & ebed)
    # unio
print(reggeli | ebed)
    # különbség
print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)
    
  
  