useransf = "Akkor menj inenn!! >:("
oszt = "A szám osztható "
e3 = "hárommal"
e4 = "néggyel"
oszt3 = oszt, e3, "."
oszt4 = oszt, e4, "."
osztmind = oszt, e3, "és", e4, "."
osztfail = "A szám nem osztható se", e3, "se", e4, "."
userans = input("Adj meg egy számot és én kiírom, hogy hárommal vagy néggyel osztható vagy sem a számod. Benne vagy? ")
if userans == "Y":
    usernum = int(input("Adj meg egy számot: "))
    if usernum % 3 == 0:
        print(oszt3)
    elif usernum % 4 == 0:
        print(oszt4)
    elif usernum % 3 == 0 and usernum % 4 == 0:
        print(osztmind)
    else:
        print(osztfail)
else:
    print(useransf)