def óraperc(szam):
    while szam > 60:
        szam - 60 = szam
        óra = óra + 1
    perc = szam  
    return int(óra) + ' óra ' + int(perc) + ' perc'