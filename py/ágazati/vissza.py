vissz_sz = int(input("adjon meg egy számot "))

while vissz_sz == 0: 
    print(vissz_sz)
    vissz_sz = vissz_sz - 1
    
    valasz = input('Mondjam még egyszer? (i/n)')    
    if valasz == 'n':
            folytatja = False
    print( " vége ")