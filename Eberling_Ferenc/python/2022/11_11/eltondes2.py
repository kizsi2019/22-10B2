lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
	if lista[index] == 'piros':
		talalat = True
	index = index + 1

if talalat:
	print('Van a listában piros szín, az indexe: ', index-1)
else:
	print('Nincs a listában piros szín.')