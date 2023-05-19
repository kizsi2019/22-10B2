def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

mondat = " ez egy példa mondat"
szavak = szavak_szama(mondat)
print(szavak)