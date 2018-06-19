'''
Created on Jul 19, 2014

@author: HOME
The script to show 1) l.insert(i,x), 2) l.pop(), 3) l.pop(i), 4) del statement
'''
lsta=[23,'anna','jana','rock',34,32,2]
for x in lsta:
    print("index value ",lsta.index(x)," : ",x)
print("#"* 40,"\n")
lsta.insert(2,5)
for x in lsta:
    print("index value ",lsta.index(x)," : ",x)
print("#"* 40,"\n")
print(lsta)
lsta.pop() # removed 2, the rightmost element in the list
print(lsta)
lsta.pop() # removed 32
print(lsta)
lsta.pop(3) # removed 'jana', the element with index value of 3, slice syntax not applicable
print(lsta)
del lsta[2:4] # remove/delete elements by index, with slice syntax also
print(lsta)