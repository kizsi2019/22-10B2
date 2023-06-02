def legnagyobb(list):
    list = [0]
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max

list=[0,1,2,3,4,5]
leg = legnagyobb(list)
print('A lista legnagyobb eleme: ', leg)


