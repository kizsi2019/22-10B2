def legnagyobb(list):
    max = list[0]

    for elem in list:
        if elem > max:
            max = elem
    return max


list = [1, 2, 3, 4, 1, 2, 3, 4, 6, 10, 90,]
leg = legnagyobb(list)
print("A lista legnagyobb eleme:",(leg))


