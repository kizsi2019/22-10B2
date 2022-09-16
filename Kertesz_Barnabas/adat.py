import time
adat = input("Adj meg egy számot!" )
szam = int(adat)

print("Ezt a számot mondatad", szam)
adat2 = input("Adj meg még egy számot!" )
szam2 = int(adat2)
print("Ezt a számot mondatad", szam2)
print("Most összeadom őket pillanatot kérek")
time.sleep(3)
print(szam+szam2)

time.sleep(2)
print("Most kiszámolók neked a végeredményel egy két műveletet")
time.sleep(2)

x = szam
y = szam2

print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x % y)

time.sleep(2)


szo1 = 'Alma'
szo2 = "fa"

print(szo1 + szo2)

print("Köszi hogy ki probáltál")