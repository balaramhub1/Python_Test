'''
Created on Apr 29, 2014

@author: ROCKSTAR
'''
#This script is to check the input number is prime or composite.
print("Script to check if a number is prime or composite")
n=int(input("Enter the number : "))
for i in range(2,n):
    if n%i==0:
        x=False
    else:
        x=True
if x==True:
    print("The number entered is prime")
else:
    print("The number entered is composite")        
        
    