szoveg1 = input("Jön Henrik ma kosarazni? (i/n) ")
szoveg2 = input("JÖn Hanna kosarazni? (i/n) ")
if szoveg1 == 'i' and szoveg2 == 'i':
    print("Mind a ketten jönnek kosarazni")
if szoveg1 == 'n' and szoveg2 == 'n':
    print("Egyikük sem jön kosarazni")
else:
    print("Egyikük jön kosarazni")
if szoveg1 == ('i' and szoveg1 == 'n') or ('n' and szoveg2 == 'i') :
    print("Valamelyikük jön kosarazni")