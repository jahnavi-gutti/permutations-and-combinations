#(substring can be possible) by combinations
from itertools import combinations
s=input()
a=[]
for i in range(1,len(s)+1):
    c=combinations(s,i)
    a.extend(c)
k=[]
for g in a:
    s="".join(g)
    k.append(s)
print(k)
    
"""
o/p:
janu
['j', 'a', 'n', 'u', 'ja', 'jn', 'ju', 'an', 'au', 'nu', 'jan', 'jau', 'jnu', 'anu', 'janu']
"""

