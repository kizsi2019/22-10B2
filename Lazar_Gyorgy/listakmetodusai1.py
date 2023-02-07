nyelvek = ['Python', 'C', 'C++', 'C#', 'Java']
nyelvek_honlapkészytéshez = ['HTML', 'CSS', 'JavaSrcipt']
#nyelvek.sort()
#nyelvek.reverse()
#print(nyelvek)
#print(nyelvek.index('Python'))
print(nyelvek.count('Pytohn'))
nyelvek.append('Python')
print(nyelvek)
nyelvek_masolat = nyelvek.copy()
print(nyelvek_masolat)
nyelvek.extend(nyelvek_honlapkészytéshez)
print(nyelvek)