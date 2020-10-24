'''
Created on Jun 14, 2020

Create Dictionary from lists

@author: beherb2
'''

l1=[1,2,3,4,5]
l2=[1,4,9,16,25]

# Create a dictionary by takeing keys from l1 and values from l2
d1=dict(zip(l1,l2))

print("Dictionary d1 is : ",d1)


d2=dict.fromkeys(l1,6)
print("Dictionary d2 is : ",d2)


# Combine 2 dictionaries
d3={1:1,2:4,3:9}
d4={4:16,5:25}

# update(), method does'nt return anything, it modifies the original Dictionary
d3.update(d4)

print("Dictionary d3 is : ",d3)


