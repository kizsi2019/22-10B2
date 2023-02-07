
'''
    Tuple:
    - rendezett (elemeknek indexe van)
    - egy elem többször szerepelhet
    - többféle típust tárolhat egyszerre is
    - NEM megváltoztatható adattípus
      (NEM lehet az elemeket módosítani, elemek sorrnedjét, számát változtatni)
    '''
    
    # tuple létrehozása
kozeppont = (0, 5)
    
    # de ez is tuple-t eredmenyez
kozeppont = 0, 5

    # hivatkozás a tuple egy elemére
print(kozeppont[1])  # 5
    
    # tuple "kicsomagolása"
x, y = kozeppont  # x értéke: 0, y értéke: 5
print(x)
print(y)  