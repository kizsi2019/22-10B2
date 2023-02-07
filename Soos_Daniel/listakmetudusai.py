nyelvek = ['Python','Python', 'C', 'C++', 'C#', 'Java']
nyelvek_honlapkészítéshrz =['HTML', 'CSS', 'Javascript']
#nyelvek.sort()
#nyelvek.reverse()
#print(nyelvek)
#print(nyelvek.index('Pyton'))
print(nyelvek.count('Python'))
nyelvek.append('Python')
print(nyelvek)
nyelvek_masolat = nyelvek.copy()
print(nyelvek_masolat)
nyelvek.extend(nyelvek_honlapkészítéshrz)
print(nyelvek)