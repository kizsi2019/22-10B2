import random

erme = input(" válasz hogy fej vagy irás ( i/f) : ")

gép = random.randint(1, 2)

if erme == "i" and gép == 1:
    print("Irás")
elif erme == "f" and gép == 1: 
    print(" ez sajna irás volt ")

if erme == "f" and gép == 2:
    print("Fej")
elif erme == "i" and gép == 2:
    print("Ez sajna fej volt")
