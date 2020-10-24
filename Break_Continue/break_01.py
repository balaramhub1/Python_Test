'''
Created on Aug 6, 2014

@author: rocky
Script to demonstrate "break" statement.
'''
from math import sqrt
print("Start of part A...")
for n in range(99,0,-1):
    root=sqrt(n)
    if root==int(root):
        print("Root of {0} is {1} ".format(n,root))
        break
print("End of part A...")
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(root):
        print("Root is : ",n)
        break
else:
    print("Did'nt find..")