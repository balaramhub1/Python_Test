'''
Created on Apr 23, 2014

@author: ROCKSTAR
'''
# This script is to check control flow by if statement.
a=input("Enter the first number -a-: ")
b=input("Enter the second number -b-: ")
c=input("Enter the third number -c-: ")

if a>b:
# print("a is greater than b")
    if a>c:
        print("a is greater than b and c")
elif b>c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")
print("----- Thank you !!")
            