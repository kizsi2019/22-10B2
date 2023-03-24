nyelvek = []
    with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            nyelv = {'evszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
            nyelvek.append(auto)

    print(f'{nyelvek=}')