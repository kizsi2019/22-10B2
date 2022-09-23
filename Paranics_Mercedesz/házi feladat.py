szam=int(input("Adj meg egy számot!"))
if szam % 3 == 0 and szam % 4 == 0:
    print("A szám hárommal és néggyel is osztható!")
elif szam % 3 == 0:
    print("A szám osztható hárommal")
elif szam % 4 == 0:
    print("A szám osztható néggyel")
else:
    print("Sem hárommal sem néggyel nem osztható")

