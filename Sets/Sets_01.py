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
