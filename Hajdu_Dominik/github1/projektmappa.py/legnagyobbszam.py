def legn(list):
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
legn = legn(list)
print("A legnagyobb szám a listában", legn)