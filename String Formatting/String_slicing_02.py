'''
Created on Jul 15, 2014

@author: HOME
String Slicing part 2
Syntax:
string[start]
string[start:end]
string[start:end:step] 

All the above is alos applicable for Sequences
'''
str1="String Slicing"
slen=len(str1)
print("Value of Str1 = ",str1)
print("Length of Str1 = ",slen)
print(str1[0:10:2])
print(str1[0:10:1])
print(str1[0:13:2])
print(str1[0:14:4])
print(str1[0:13:3])
print(str1[:13:3])
print(str1[3:13:2])
#print(str1[3:13:-2])
print(str1[-1:-15:-1])
print(str1[-1:-15:-2])
