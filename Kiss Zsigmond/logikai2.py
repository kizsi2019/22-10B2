szoveg1 = input("Jön Henrik ma kosarazni? (i/n) ")
szoveg2 = input("Jön Hanna ma kosarazni? (i/n) ")

if szoveg1 == 'i' and szoveg2 == 'i':
    print("Mind a ketten jönnek kosarazni")
if szoveg1 == 'n' and szoveg2 == 'n':
    print("Egyikük sem jön kosarazni")
if (szoveg1 == 'i' and szoveg2 == 'n') or (szoveg1 == 'n' and szoveg2 == 'i') :
    print("Valamelyikük jön kosarazni")
