'''
Created on Jul 17, 2014

@author: HOME
This script is to use str.format() method in ifelsetest_02.py script
'''
# This script is to check control flow by if statement.
a=input("Enter the first number -a-: ")
b=input("Enter the second number -b-: ")
c=input("Enter the third number -c-: ")

if a>b:
# print("a is greater than b")
    if a>c:
        print("a '{0}' is greater than b '{1}' and c '{2}' ".format(a,b,c))
elif b>c:
    print("b '{1}' is greater than a '{0}' and c '{2}' ".format(a,b,c))
else:
    print("c '{2}' is greater than a '{0}' and b '{1}' ".format(a,b,c))
    print(" Thank you !!")
            