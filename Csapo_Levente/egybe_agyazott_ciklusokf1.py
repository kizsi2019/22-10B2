szam = int(input("Adj meg egy páros számot! "))

sor = 1
while sor <= 8:
      oszlop = 1
      while oszlop <= szam/2:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      szam = szam + 1
      sor = sor + 1