#(substring can be possible) by permutations
from itertools import permutations
s=input()
a=[]
for i in range(1,len(s)+1):
    p=permutations(s,i)
    a.extend(p)
k=[]
for g in a:
    s="".join(g)
    k.append(s)
print(k)
"""
janu
['j', 'a', 'n', 'u', 'ja', 'jn', 'ju', 'aj', 'an', 'au', 'nj', 'na', 'nu', 'uj', 'ua', 'un', 'jan', 'jau', 'jna', 'jnu', 'jua', 'jun', 'ajn', 'aju', 'anj', 'anu', 'auj', 'aun', 'nja', 'nju', 'naj', 'nau', 'nuj', 'nua', 'uja', 'ujn', 'uaj', 'uan', 'unj', 'una', 'janu', 'jaun', 'jnau', 'jnua', 'juan', 'juna', 'ajnu', 'ajun', 'anju', 'anuj', 'aujn', 'aunj', 'njau', 'njua', 'naju', 'nauj', 'nuja', 'nuaj', 'ujan', 'ujna', 'uajn', 'uanj', 'unja', 'unaj']
"""

