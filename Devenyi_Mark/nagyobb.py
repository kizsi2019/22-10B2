def legnagyobb(list):
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max


list = [1,2,3,4,5,6,7,8,9,10]
ln = legnagyobb(list)
print("list legnagyobb eleme",ln)
