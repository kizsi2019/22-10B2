szoveg1 = input("Jön Henrik  ma kosarazni? (I/N) ")
szoveg2 = input("Jön Hanna  ma kosarazni? (I/N) ")
# 2 Yes
if szoveg1 == 'I' and szoveg2 == 'I':
    print("Mindketten jönnek kosarazni")
# 2 No
if szoveg1 == 'N' and szoveg2 == 'N':
    print("Senki nem jön kosarazni")
# 1 Yes or 1 No
if szoveg1 == 'I' and szoveg2 == 'N':
    print("Csak Henrik jön kosarazni")
# 1 No or 1 Yes
if szoveg1 == 'N' and szoveg2 == 'I':
    print("Csak Hanna jön kosarazni")
