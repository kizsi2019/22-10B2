
with open('nyelvek.txt', 'r') as fki, \
        open('nyelvek_masolat.txt', 'w') as fbe:
    for sor in fbe:
        adatok = sor.strip().split(";")
        fki.write(adatok[1] + ";" + adatok[0] + "\n")