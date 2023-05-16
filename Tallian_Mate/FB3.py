
def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

mondat = input("Adj meg egy szöveget.")
szavak = (szavak_szama(mondat))
print(szavak)

