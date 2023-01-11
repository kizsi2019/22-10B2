szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
darab = 0
for szo in szavak:
    if szo[0] == "A" or szo[0] == "a":
        darab += 1
print("Ennyi darab A vagy a kezdőbetűs szó van a listában:", darab)