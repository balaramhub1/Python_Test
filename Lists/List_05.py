'''
Created on Jul 19, 2014

@author: HOME
The script to show functioning of 1) l.remove(x), 2) l.sort(), 3) l.reverse().
'''
lsta=[2,3,5,0,9]
lstb=['zeb','kite','ball','truck']
print(lsta)
print(lstb)
lsta.remove(5)
lstb.remove('ball') # throws error if element not found
print(lsta)
print(lstb)
lsta.sort()
lstb.sort()
print(lsta)
print(lstb)
lsta.reverse() # same as l.sort(reverse=True)
lstb.reverse()
print(lsta)
print(lstb)