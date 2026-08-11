from itertools import product
k = 0
m = []
for p in product(sorted("АКЦЕНТ"), repeat=5):
    k += 1
    s = ''.join(p)
    if s[0] != 'А' and s[0] != 'Е' and s[0] != 'К' and s.count('Т') >= 1:
           print(k)
           break