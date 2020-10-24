'''
Created on Jun 14, 2020

Removing elements from dictionary by using
- pop()
- popitem()
- clear()
- del()

@author: beherb2
'''
d1={1:1,2:4,3:9,4:16,5:25,6:36}

print("Dictionary d1 is : ",d1)

# remove any specific element by key

# removes and returns the value with key as 2
d1.pop(2)
print("Dictionary d1 after removing the element with key as 2 :",d1)

# removes and returns the last key,value pair as tuple
print(d1.popitem())
print("Dictionary d1 after removing the last element :",d1)

# Clear all the contents of the dictionary
d1.clear()
print("Dictionary after clear() is : ",d1)

# Delete the dictionary d1
del d1
print("Dictionary after clear() is : ",d1)


