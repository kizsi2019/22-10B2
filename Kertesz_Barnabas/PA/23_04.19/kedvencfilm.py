def óraperc(self, óra , perc): 
    perc = perc * 60
    if óra % 2:
        print
    return str(óra) + ' óra ' + str(perc) + ' perc'


Film = input("Add meg egy film címét!")
Perc = input("Hány perces a film?")
print("A(z)", Film ,"című film" , óraperc , "hosszú")
