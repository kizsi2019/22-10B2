with open('bemenet.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            celfajl.write(adatok[0] + ';' + adatok[1] + '\n')
print("A fájlok exportálása sikeres!")
            