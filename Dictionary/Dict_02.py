'''
Created on Jul 21, 2014

@author: HOME
The script is to show Dictionary methods 1)D.get(key), 2) D.get(key,value)
3) D.pop(key) , 4) D.pop(key,value) 
'''
Da={'apple': 4,'orange': 6,'cherry':10,'grapes':20}
print(Da)
print(Da.get('cherry'))
print(Da.pop('orange'))
print(Da)
Db=Da.copy()
print(Db)
Da.clear()
print(Da)