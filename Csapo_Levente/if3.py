import random

gondolt_szam = random.randint(1, 5)
szam = int(input("Írj be egy számot! "))
print(f'A gondolt szám: {szam}')  

if gondolt_szam == szam:
    print("A kettő szám egyenlő!")
elif gondolt_szam < szam:
    print("Kisebb a gondolt szám!")
else:
    print("A beírt szám kisebb!")