'''
Created on Jun 6, 2020

Demonstrate enumerate to access index and value of elements in iterable data structure.

@author: beherb2
'''
l1=[2,4,6,8,10,12,14,16]
print("List is : ",l1)

print("Elements of list are : ")
for x in l1:
    print(x)


for i,v in enumerate(l1):
    print("Element at -",i,"is : ",v)


