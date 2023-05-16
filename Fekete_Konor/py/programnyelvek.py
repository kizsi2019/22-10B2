nyelvek = []

with open("progamny.txt", "r") as f_be, \
        open("programm.txt" , "w") as fki:
    for sor in f_be:
        adatok = sor.strip().split(";")
        fki.write(adatok[1] + ";" + adatok[0] + "\n")
