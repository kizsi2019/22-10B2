# fajl megnyitása
forrasfajl = open('python/autok_listaja.csv')

# fájl tartalmának beolvasása
# egy sor beolvasása:
forrasfajl.readline()

# a teljes fájltartalom beolvasása
# listával tér vissza, a sorok a lista elemei
forrasfajl.readlines()

# a teljes fájltartalom beolvasása
forrasfajl.read()

# a fájlobjektum tartalmanak bejarasa
for sor in forrasfajl:
    print(sor)

# fájl bezárása    
forrasfajl.close() 