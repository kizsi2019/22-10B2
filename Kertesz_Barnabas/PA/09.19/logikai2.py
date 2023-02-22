szoveg1 = input("Jön Henrik  ma kosarazni? (I/N) ")
szoveg2 = input("Jön Hanna  ma kosarazni? (I/N) ")
if szoveg1 == 'I' and szoveg2 == 'I':
    print("Mindketten jönnek kosarazni")
if szoveg1 == 'N' and szoveg2 == 'N':
    print("Senki nem jön kosarazni")
if szoveg1 == 'I' and szoveg2 == 'N':
    print("Csak Henrik jön kosarazni")
if szoveg1 == 'N' and szoveg2 == 'I':
    print("Csak Hanna jön kosarazni")
