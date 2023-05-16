import random
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

print("A legnagyobb szám és a legkisebb szám különbsége: ", nezo(szaml))