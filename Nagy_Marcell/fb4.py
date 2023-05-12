
def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

mondat = "Adj meg egy szöveget."

print(szavak_szama(mondat))