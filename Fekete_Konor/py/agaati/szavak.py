szo1 = input("adj meg egy szót! ")
szo2 = input("adj meg még egy számot ")

if  len(szo1) > len(szo2):
    print("a Hosszabb szó :", szo1) 
elif len(szo1) < len(szo2):
    print("a hosszabb  szó : ", szo2)
else :
    print("A két szó egyforma hosszó")