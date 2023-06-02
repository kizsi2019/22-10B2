def legnagyobb(list):
    max = list[0]
    for lm in list:
        if lm > max:
            max = lm
    return max


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lm = legnagyobb(list)
print("list legnagyobb lm",lm)