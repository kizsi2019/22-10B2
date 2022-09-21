Folytatja = True
szamlalo = 1 
while szamlalo <= 5:
    print("Programozni jó")
    szamlalo += szamlalo


while Folytatja:
    print("akarja újra futtatni ? ")
    valasz = input("Igen vagy nem (N/I)")
    if valasz == "N":
        Folytatja = False
print (" >>> A Program véget ért <<<")