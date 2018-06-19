'''
Created on Jul 15, 2014

@author: HOME
'''
str1="String Slicing"
slen=len(str1)
print("Length of Str1 = ",slen)
print(str1[:]) # displays the complete string.
print(str1[0:])  # displays the complete string.
print(str1[0:slen]) # displays the complete string.
print(str1[0:slen-2])
print(str1[2:slen-2])
print(str1[3:slen-4])
print(str1[3:12])
print(str1[3:0]) # will not display any thing.
print(str1[3:6])
print(str1[3:-3])
print(str1[-9:-3])
print(str1[-1])