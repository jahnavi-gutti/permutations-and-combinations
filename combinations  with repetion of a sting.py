#(substring can be possible) by combinations with repetion
from itertools import combinations_with_replacement
s=input()
a=[]
for i in range(1,len(s)+1):
    c=combinations_with_replacement(s,i)
    a.extend(c)
k=[]
for g in a:
    s="".join(g)
    k.append(s)
print(k)
    
    
"""
o/p:
janu
['j', 'a', 'n', 'u', 'jj', 'ja', 'jn', 'ju', 'aa', 'an', 'au', 'nn', 'nu', 'uu', 'jjj', 'jja', 'jjn', 'jju', 'jaa', 'jan', 'jau', 'jnn', 'jnu', 'juu', 'aaa', 'aan', 'aau', 'ann', 'anu', 'auu', 'nnn', 'nnu', 'nuu', 'uuu', 'jjjj', 'jjja', 'jjjn', 'jjju', 'jjaa', 'jjan', 'jjau', 'jjnn', 'jjnu', 'jjuu', 'jaaa', 'jaan', 'jaau', 'jann', 'janu', 'jauu', 'jnnn', 'jnnu', 'jnuu', 'juuu', 'aaaa', 'aaan', 'aaau', 'aann', 'aanu', 'aauu', 'annn', 'annu', 'anuu', 'auuu', 'nnnn', 'nnnu', 'nnuu', 'nuuu', 'uuuu']
"""

