'''
Created on Jun 6, 2020

Demonstrates the usage of membership operators : in, not in

@author: beherb2
'''

l1=[10,20,30,40,50]

if(100 in l1):
    print("Element is Available ")
else:
    print("Element is not available")
    

print(10 in l1)

print(11 not in l1)

s= "Hello how are you"
print("String value is :",s)
print("Check 'how' is available in the string")
print("how" in s)
