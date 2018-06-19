'''
Created on Jan 28, 2015

@author: rocky
Script to check for Armstrong Number
'''
total=0
n=int(input("Enter the Number : "))
temp=n
while(n>0):
    digit=n%10
    total=total + digit**3
    n=n//10
if(temp==total):
    print(temp,": is Armstrong Number ")
else:
    print(temp,": is Not Armstrong Number")
