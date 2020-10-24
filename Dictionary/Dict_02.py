'''
Created on Jul 21, 2014

@author: HOME
The script is to show Dictionary methods 1)D.get(key), 2) D.get(key,value)
3) D.pop(key) , 4) D.pop(key,value) 
'''
Da={'apple': 4,'orange': 6,'cherry':10,'grapes':20}
print(Da)
print("No of Cherry is :",Da.get('cherry'))
print("After removing orange")
print("No of Orange is :",Da.pop('orange'))
print(Da)
Da.update({'apple':5})
print("After updating apple count..")
Db=Da.copy()
print(Db)
Da.clear()
print(Da)
print(Db)
Db.popitem()
print(Db)