nyelvek = []
with open('feladat10.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'evszam': int(adatok[0]), 'pr_nyelv': adatok[1],
                'Lastname': adatok[2]  'Firstname': adatok[3]}
        nyelvek.append(nyelv)

print(f'{nyelvek=}')
