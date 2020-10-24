'''
Created on Jul 23, 2014

@author: HOME
'''
import random
n=int(input("Enter a number : "))
num=n+random.randint(3,30)
print("Value of random num is : ",num)
if num>=20 or num<=10:
    print("num value is less than 10 or greater than 20")
else:
    print("num value is between 10 to 20 ")
