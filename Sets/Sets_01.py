'''
Created on Jul 21, 2014

@author: HOME
'''
s1={1,2,3,'df','sdf',4,5}
s2={5,9,'apple','orange','df'}
s1.add('orange')
print(s1)
print(s1.difference(s2))
print(s1-s2)
print(s1.difference_update(s2))

# Union operation

s3=s1.union(s2)
print(s3)

# Intersection operation between sets
s1.add("df")
s1.add(9)
s4=s1.intersection(s2)
print(s4)


