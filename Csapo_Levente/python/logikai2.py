henrik_kerdes = input("Henrik jön ma kosarazni? (igen/nem)")
hanna_kerdes = input("Hanna jön ma kosarazni? (igen/nem)")

if henrik_kerdes == 'igen' and hanna_kerdes == 'igen':
    print("Az ikrek jönnek kosarazni!")
elif henrik_kerdes == 'igen' or hanna_kerdes == 'igen':
    print("Nem mindketten jönnek kosarazni!")
else:
    print("Nem jönnek kosarazni!")