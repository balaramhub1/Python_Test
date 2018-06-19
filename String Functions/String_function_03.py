'''
Created on Jul 15, 2014

@author: HOME
The script is to see the function of s.split(t,n) method.
'''
str1="hello how are you, i am fine here ,are you coming, else good bye"
str2="hello, how, are, you"
print(str1.split('y'))
#splits at y and returns a list of strings. y excluded
print(str1.split('y',2))
print(str1.split('are',2))
print(str1.split())
print(str2.split(','))
print(str2.split(',',2))

