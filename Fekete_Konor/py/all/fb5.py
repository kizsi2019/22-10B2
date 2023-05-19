import random

def min_max(list):
    min = list[0]
    max = list[0]

    for elem in list:
        if elem < min:
           min = elem
        if elem > max:
           max = elem 
    return max - min

#lista = [ 2,3,4,5,6,3#


print(" legnagyobb és lekisebb közöti külömbség ", min_max(lista))