ora = input("Ennyi óra van")
ora = int(ora)
if ora >= 8 and ora < 16:
    print('A bolt nyitva')
    meg_ennyi_ideig_nyitva = 16 - ora
    print('Ennyi órád van még odaéerni:', meg_ennyi_ideig_nyitva)
else:
    print('A bolt zárva')