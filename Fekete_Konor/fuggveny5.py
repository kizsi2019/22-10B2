szam = int(input("Adja meg egy számot "))
szamok = []
while szam > 0:
        szamok.append(szam)
        szam = int(input("ajd meg egy szamot : "))
def min(szamok):
    min=szamok[0]
    for item in szamok: 
        if item < min:
            min = item  
    return min

    
print(szamok)
print("A lista legkisebb eleme : " , min(szamok))             

def max(szamok):
    max=szamok[0]
    for item in szamok: 
        if item > max:
            max = item  
    return max
print("Lista Legnagyobb száma : " , max(szamok))

def osszegzo(szamok):
    osszeg = 0
    for item in szamok: 
        osszeg += item
    return osszeg



print("A számok összeg : " , osszegzo(szamok))