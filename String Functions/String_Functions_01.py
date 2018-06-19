'''
Created on Jul 15, 2014

@author: HOME

This script covers String methods like  1) s.capitalize(), 2) s.title()
3) s.count(t,start,end), 4) s.find(t,start,end), 5) s.index(t,start,end)
'''
str1="stRing teSt"
str2="stRing teSt for Python leArNing and dEveLopment"
print("String length of str2 is : ",len(str2))
print("Original String is : ",str1)
print("Capitalized String is : ",str1.capitalize())
print("Capitalized String using title() is : ",str1.title())
print("count of alpahbet 't' in str2 is : ",str2.count('t'))
print("count of alpahbet 't' in str2 is : ",str2.count('t',0,16))
print("count of alpahbet 'e' in str2 is : ",str2.count('e',16,46))
print("count of alpahbet 'E' in str2 is : ",str2.count('E',16,46))
print("Left most position of P in str2 is : ",str2.find('P'))
print("Left most position of t in str2 is : ",str2.find('t'))
print("Left most position of e in str2 is : ",str2.find('e'))
print("Left most position of E in str2 is : ",str2.find('E'))
print("Left most position of z in str2 is : ",str2.find('z'))
print("Left most position of t in str2 is : ",str2.find('t',2,15))
print("Left most Index of P in str2 is : ",str2.index('P'))
print("Left most Index of t in str2 is : ",str2.index('t'))
print("Left most Index of e in str2 is : ",str2.index('e'))
print("Left most Index of E in str2 is : ",str2.index('E'))
print("Left most Index of t in str2 is : ",str2.index('t',2,15))
print("Left most Index of z in str2 is : ",str2.index('z'))
