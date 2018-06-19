
'''
Created on Jan 28, 2015

@author: rocky
Script to find the sum of digits of a number.
'''
n=int(input("Enter the Number : "))
temp=n
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("Sum of digits of",temp,"is",total)