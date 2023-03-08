szo = int(input("adj meg egy szót! "))
szo2 = int(input("adj meg egy szót! "))
if szo > szo2:
    print(szo, "hosszabb mint", szo2)
elif szo < szo2:
    print(szo2, "hosszabb mint", szo)
else:
    print("mind a kettő szó egyenló hosszuságú")