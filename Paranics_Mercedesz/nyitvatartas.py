óra = input('Hány óra van most?')
óra = int(óra)
if óra >= 8 and óra < 16:
    print('A bol nyitva van')
    még_ennyit_van_nyitva= 16-óra
    print('Ennyi órád van még odaérni:', még_ennyit_van_nyitva)
else:
    print('A bolt zárva')