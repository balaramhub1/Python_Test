'''
Created on Feb 13, 2015

@author: Administrator

working of search function of regular expression
-in single line
-in multiline
'''
import re 
pat1='are'
s='''these are the scripts to find are and are \n
second line of string are ended \n
third line of string \n
'''
result1=re.search('are',s)
print(result1)
result2=re.search('^these',s)
print(result2)
result3=re.search('^are',s)
# checks for 'are' in start of line.
print(result3)
result4=re.search('^second',s,re.MULTILINE)
#checks for 'second' in start of lines.(in multiline mode )
print(result4)
