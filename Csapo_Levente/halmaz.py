reggeli = {'tea', 'vaj', 'piritós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True])  
reggeli.add('lekvár')
reggeli.pop()
reggeli.remove('sajt')
reggeli.discard('sajt')
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)