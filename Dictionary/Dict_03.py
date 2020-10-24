'''
Created on Jun 14, 2020

@author: beherb2
'''
Da={'apple': 4,'orange': 6,'cherry':10,'grapes':20}
print("Dictionary Da values are : ",Da)

print(Da.get("apple"))

print(Da.setdefault("orange"))
print(Da.get("orange"))

'''
get() and setDefault() method returns the value as per the passed 'key'
But if the 'key' provided is not available 

get() - returns None
setdefault() - adds the 'key' with value as 'None' into the Dictionary and returns the resulting Dictionary.

'''

print(Da.get("apple1"))

print(Da)

print(Da.setdefault("apple1"))

print(Da)