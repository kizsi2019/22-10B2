Henrik = input("Henrik jön ma kösarazni (I/N) : ")

Hanna = input("Hanna jön ma kosarazni (I/N) : " )

if Henrik == "I" and Hanna == "I":
    print("Mind a ketten jönnek kosarazni")

if Henrik == "I" and Hanna == "N":
    print( "csak egyiköjük jönn" )
elif Henrik == "N" and Hanna == "I":
    print("Csak az egyikük")

if Henrik == "N" and Hanna == "N":
    print("Egyik sem jönn")