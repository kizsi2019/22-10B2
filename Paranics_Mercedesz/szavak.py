szo = (input('Adj meg egy szót!'))
szo2 = (input('Adj meg egy másik szót! '))
if len(szo) < len(szo2):
    print(' A hosszab szo:', szo2)
elif len(szo) > len(szo2):
    print('A hosszab szo:', szo)
else:
    print('A két szo egyenlő')

