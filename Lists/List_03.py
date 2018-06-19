'''
Created on Jul 19, 2014

@author: HOME
# Script to see list methods
1) l.append(x), 2) l.count(x), 3) l.extend(m), 4) l+=m, 5) l.index(x,star,end)
'''
lista=['a',3,'c','a','tiger']
listb=['inta','charb']
listc=['b','c','e',2,8,'f','h','j','c',(1,2),'c',['d','c','y']]
print(lista)
lista.append(7)
print(lista)
print(lista.count('a'))
lista.extend(listb)
print(lista)
print(listc.index('c')) # index of leftmost 'c'
print(listc.index('c',5,11))
print(listc.index('c',9,11))


