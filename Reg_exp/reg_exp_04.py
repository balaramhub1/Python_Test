'''
Created on Mar 15, 2015
Script to find a emai id in a line of text by using regular expression

@author: Administrator
'''
import re
st='''The Python module re provides abc.xyz@gmail.com another great email.mail@mail.com method, 
which other languages like Perl and Java lgsi-lge@lge.com don't provide. 
If you want to find tree_one@yahoo.com all the substrings in a string, which 
match a regular expression, you have to use a loop in Perl 
and other languages, as can be seen in the following Perl snippet'''

print("Search with Pattern = '[\w]+@[\w]+' ")
pat1='[\w]+@[\w]+'
m1=re.search(pat1, st,re.IGNORECASE)
# re.MULTILINE has no effect as search will only work for first match in a single line 
print(m1)
# O/P: <_sre.SRE_Match object; span=(34, 43), match='xyz@gmail'>
print(m1.group())
# O/P: xyz@gmail
m2=re.findall(pat1, st, re.IGNORECASE)
print(m2)
# displays all the matches as a List
# O/P: ['xyz@gmail', 'mail@mail', 'lge@lge', 'tree_one@yahoo']
print("Search with Pattern = '[\w.]+@[\w.]+' ")
pat2='[\w.]+@[\w.]+'
m3=re.search(pat2, st, re.IGNORECASE)
print(m3)
# O/P: <_sre.SRE_Match object; span=(30, 47), match='abc.xyz@gmail.com'>
print(m3.group())
# O/P: abc.xyz@gmail.com
m4=re.findall(pat2, st, re.IGNORECASE)
print(m4)
# O/P: ['abc.xyz@gmail.com', 'email.mail@mail.com', 'lge@lge.com', 'tree_one@yahoo.com']
pat3='[\w.-]+@[\w.]+'
m5=re.findall(pat3, st, re.IGNORECASE)
print(m5)
# pattern to group the searched items.
pat4='([\w.-]+)@([\w.]+)'
m6=re.findall(pat4, st, re.IGNORECASE)
print(m6)

