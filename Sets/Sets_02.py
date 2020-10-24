'''
Created on Jan 23, 2020

@author: beherb2
'''
A={1,4,7,12,45,74}
print("Set is : ",A)

A.update([2,8,99])
print("Updated set is :",A)

print("Length of Set is : ",len(A))

for x in A:
    if x>40:
        print("{0} is greater than 40".format(x))
    else:
        print("{0} is less than 40".format(x))

B={4,45}
C={102,104,"abcd",66,"tty"}

if A.isdisjoint(C):
    print("Set A and C are disjoint")

if B.issubset(A):
    print("Set B is subset of A")
     

# Delete the Set
del C
   
print(C) # will throw an exception.
print("End of Script")
     
