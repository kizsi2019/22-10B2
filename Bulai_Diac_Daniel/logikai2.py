szoveg1 = input("jön Henrik ma kosarazni? (i/n) ")
szoveg2 = input("jön Hanna ma kosarazni? (i/n) ")

if szoveg1 == 'i' and szoveg2 == 'i':
    print("Mind a ketten jönnek kosarazni")
if szoveg1 == 'n' and szoveg2 == 'n':
    print("egyikük sem jön kosarazni")
if  (szoveg1 == 'i' and szoveg2 == 'n') or (szoveg1 == 'n' and szoveg2 == 'i') :
    print("valamelyik megy kosarazni")