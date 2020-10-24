'''
Created on Jun 6, 2020

This script is to demonstrate the Comparision operators ( ==,!=,<=,>= )

@author: beherb2
'''

a=5
b=6
c=5
d='N'
e='n'
f='N'
g="Hello"
h="Hello"
i="wow"

print("Check if a = c : ", a==c)

print("Check if a = b : ", a==b)

# Check equality using - is - or - is not -

print("Check if a = c : ", a is c)

print("Check if a = b : ", a is not b)

l1=[10,20,30]
l2=[10,20,30]

# check if l1 = l2

print("Check if l1 = l2 : ", l1 == l2)

# Below will return False, as 'is' operator will compare the memory location.
print("Check if l1 = l2 : ", l1 is l2)


