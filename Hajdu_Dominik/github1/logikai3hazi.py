szam = int(input('Adj meg egy számot'))

if szam % 3 == 0:
    print('3mal osztható')
elif szam % 4 == 0:
    print('4el osztható')
elif szam % 3 == 0 and szam % 3 == 0:
    print('3al 4el is osztható')
else:
     szam % 3 == 0 or not szam % 3 == 0:
     print('3al és 4el se osztható') 