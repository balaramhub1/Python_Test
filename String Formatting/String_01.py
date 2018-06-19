'''
Created on Jul 14, 2014

@author: HOME
'''
''' Script to display each element of a String '''
s="waxwork hi"

print("Provided String is : ",s)
slen=len(s)
print("String lenth is :",slen)
print("\nFirst Element is : ",s[0])
print("\nSecond Element is : ",s[1])
print("\nThird Element is : ",s[2])
print("\nFourth Element is : ",s[3])
print("\nFifth Element is : ",s[4])
print("\nSixth Element is : ",s[5])
print("\nSeventh Element is : ",s[6])

i=0
for x in s:
    print("Element s[",i,"]=",x)
    i=i+1