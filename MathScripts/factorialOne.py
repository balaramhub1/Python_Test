'''
Created on Jan 28, 2015

@author: rocky
Script to find the factorial of a number
'''
n=int(input("Enter the Number : "))
fact=1
while(n>1):
    fact=fact*n
    n=n-1
print(fact)