
def szavak_list(szoveg):
    szavak = szoveg.split()
    return len(szavak)

#lista = [1,2,3,4,5,6,7,8,9,10]
#lista = [ ]
#for i in range(10):
    #szam = random.randint(0, 10)
    #lista.append(szam)
#print("A hozzáadás sikeres volt.")

mondat = input("Adj meg egy szöveget ")

print(szavak_list(mondat))
#print(lista)

