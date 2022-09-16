szam = int(input("Adj meg egy számot: "))

if szam < 0:
    print("a számod negativ ")
elif szam > 0:
    print("számod pozitiv ")
elif szam == 0:
    print("ez a szám nulla")

print("Program vége")