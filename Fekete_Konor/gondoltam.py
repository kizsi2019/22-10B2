import random

szam = random.randint(1, 5)

szam2 = int(input("Adj meg egy számot : "))

if szam2 == szam:
    print("SIkerült eltaláltad igazi gondolat olvaso vagy!!")
elif szam2 < szam:
    print("Kissebb lett a számod ....")
elif szam2 > szam:
    print("Nagyobb lett a számod ")