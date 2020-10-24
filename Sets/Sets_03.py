'''
Created on Jan 23, 2020

@author: beherb2
'''
# Creating Set using the set() constructor
A=set(("ajay","bijay","ronny","sumo"))
print("Set details are : ",A)

# Symmetric difference
s1={10,20,30,40,50,60}
s2={40,50,60,70,80,90}

# all un-common elements
s3=s1.symmetric_difference(s2)
print(s3)