'''
Created on Mar 18, 2015

@author: Administrator
'''
import re

st='''The Python module re provides another great method, 
which other languages like Perl and Java don't provide. 
If you want to find all the substrings in a string, which 
match a regular expression, you have to use a loop in Perl 
and other languages, as can be seen in the following Perl snippet'''
m1=re.match('the', st, re.IGNORECASE)
print("Printing the value of Match m1 : ")
print(m1)
print("++++++++++++++++++++++++++++++++++++++++")
print("Printing the Matched object : ")
print(m1.group())
print("++++++++++++++++++++++++++++++++++++++++")
m2=re.search('the', st, re.IGNORECASE)
print("Printing the value of Search m2 : ")
print(m2.group())
print("++++++++++++++++++++++++++++++++++++++++")