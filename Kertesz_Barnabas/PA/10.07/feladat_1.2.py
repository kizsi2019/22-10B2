folytatja = True
while folytatja:
    valasz = input("Adj meg egy mondatot!")
    if valasz[-1] == '.':
        print("Ez a mondat kijelentő")
    if valasz[-1] == '?':
        print("Ez a mondat kérdőjel")
    if valasz[-1] == '!':
        print("Ez a mondat kijelentő")
    if valasz == "":
        folytatja = False
print("Program vége!")