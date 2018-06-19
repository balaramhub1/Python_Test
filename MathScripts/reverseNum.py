
'''
Created on Jan 28, 2015

@author: rocky
Script to reverse the number
'''
n1=input("Enter the Number : ")
ln1=len(n1)
base=10**(ln1-1)
print(base)
n1=int(n1)
n2=0
while(n1>0):
    digit=n1%10
    n2=n2+base*digit
    base=base//10
    n1=n1//10
print(n2)
