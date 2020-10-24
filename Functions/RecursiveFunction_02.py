'''
Created on Jun 14, 2020

- using Recursive for linear search , binary search

@author: beherb2
'''

l=[100,200,300,400,500,600,700,800,900]

# binary search

def binarySearch(l,key):
    
    if len(l) == 0:
        return False
    else:
    
        mid = len(l) // 2
        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binarySearch(l[:mid], key)
        else:
            return binarySearch(l[mid + 1:], key)


result=binarySearch(l,750)
print(result)




