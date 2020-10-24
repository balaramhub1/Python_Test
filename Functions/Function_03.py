'''
Created on Jun 14, 2020

function with positional argument

No of arguments and order of arguments should be same in the function call and definition.

@author: beherb2
'''
l=[100,200,300,400,500,600]
key=4000


def searchKey(l,key):
    for x in l:
        if key==x:
            return True
        
    else:
        return False
    
    return result

result=searchKey(l,key)
print(result)