szavak = ['Alma', 'Banán', 'Kecske', 'Tó']

legrovidebb = szavak[0]
for szo in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo

print("A lista legrövidebb szava: ", legrovidebb)