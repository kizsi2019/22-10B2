with open("Timeline_of_ programming_languasges.txt", "r") as f_be, \
        open ("Timeline_of_ programming_languasges_masolat.txt", "w") as f_ki:
    for sor in f_be:
        adatok = sor.strip().split(";")
        f_ki.write(adatok[1] + ";"  + adatok[0] + "\n")