'''
Created on Aug 16, 2014

@author: rocky
Script to demo exception handling
'''
s='hello'
try:
    for st in s:
        print("String elements are : ",st)
    print("Sixth element of 's' is : ",s[6])
except:
    print("There are only 5 elements ")
