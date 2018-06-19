'''
Created on Aug 26, 2014

@author: rocky
Script to demonstrate working of regular expression in python.
match - checks for a match only at the begining of the string.
search - checks for match any where in the string.
'''
import re
pat1='how'
pat2='hello'
pat3='are'
s="hello how are you !, lif's good."
print('String is : ',s)
m=re.search(pat1,s)
print(m)
o=re.search(pat3,s)
print(o)
n=re.match(pat2,s)
print(n)
print(n.group(0))
print(m.group(0))
print(o.group(0))
