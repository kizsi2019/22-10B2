bejutott = False

while not bejutott:
    felhasználonév = input("Adja meg a felhasználo nevet ")
    jelszo = input("adja meg a jelszavát ")
    if felhasználonév == "bori99" and jelszo == "Szivecske<3":
        print("Belépés engedélyezve")
        bejutott = True
    else:
        print("belépés megtagadva")