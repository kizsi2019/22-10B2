def nezo(list):
    min = list[0]
    max = list[0]
    for elem in list:
        if min > elem:
            min = elem
        if elem > max:
            max = elem
    return max - min
szaml=[]
szam = input('Adj megf egy számot: ')
while szam != '':
    szaml.append(szam)
    szam = int(input('Adj meg egy számot: '))

print("A legnagyobb szám és a legkisebb szám különbsége: ", nezo(szaml))