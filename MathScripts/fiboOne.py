'''
Created on Jan 28, 2015

@author: rocky
Script to generate fibonacci series.
'''
r=int(input("Enter the Range : "))
f0=0
f1=1
fiboseries=[0]
for i in range(1,r):
    f=f1+f0
    f0=f1
    f1=f
    fiboseries.append(f)
print(fiboseries)
    