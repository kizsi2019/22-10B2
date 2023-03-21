szo1 = input("Adj meg egy szót! ")
szo2= input("Adj meg egy másik szót! ")
if len(szo1) > len(szo2):
    print("A hosszabb szó: ", szo1)
elif len(szo1) < len(szo2):
    print("A hosszabb szó: ", szo2)
else:
    print("A két szó egyforma hosszú")