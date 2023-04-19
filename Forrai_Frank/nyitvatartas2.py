ora = input('Hány óra van most? ')
ora = int(ora)
if ora >= 8 and ora < 16:
    print('A bolt nyitva van')
    meg_ennyit_van_nyitva = 16-ora
    print('Ennyi orad van meg odaerni:', meg_ennyit_van_nyitva)
else:
    print('A bolt zárva van')