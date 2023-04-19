egyik = input('Adj meg egy szót!')
egyik_hossza = len(egyik)
masik = input('Adj meg egy másik szót!')
masik_hossza = len(masik)
if egyik_hossza > masik_hossza:
    print('A hosszabb szó:',egyik)
elif masik_hossza >egyik_hossza:
    print('A hosszabb szó:', masik)
else:
    print('A két szó egyforma hosszú.')