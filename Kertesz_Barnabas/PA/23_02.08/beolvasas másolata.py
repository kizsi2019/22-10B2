nyelvek = []
with open('adatok/adat.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv = {'evszam': int(adatok[0]), 'pr_nyelv': adatok[1], 'Last': adatok[2], 'First': adatok[3]}
        nyelvek.append(nyelv)
print(f'{nyelvek=}')
