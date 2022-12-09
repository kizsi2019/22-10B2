szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
darab = 0
for szo in szavak:
    if szo[0] == "A" or szo[0] == "a":
        darab+=1
print("Ennyi 'A' vagy 'a' van a kezdőbetűs szó van a listában: ", darab)