autok = []
    with open('Timeline_of_ programming_languages.txt', 'r',) as f_be, \
            open_("Timeline_of_ programming_languages_masolat.txt", "w") as f_ki:
        for sor in f_be:
            adatok = sor.strip().split(';')
            f_ki.write(adatok[1] ";"_+ adatok[0] + "\n")
    