'''
Created on Feb 13, 2015

@author: Administrator

find a pattern in string using regular expression findall() function.
'''
import re
st='''The aim of this chapter of our Python \n
tutorial is to present a detailed and descriptive \n 
introduction into regular expressions. \n 
This introduction will explain the theoretical \n
aspects of regular expressions and will show you how \n
to use them in Python scripts. '''
pat1='of'
pat2='to'
pat3='This'
#re.findall('to', st, re.MULTILINE)
m1=re.search('\w+',st)
m2=re.match('\w+',st)
m3=re.findall('\w+',st)
m4=re.finditer('\w+',st)
print(m1.group())
print(m2.group())
print(m3)
for x in m4:
    print(x.group())
print("++++++++++++++++++++++++++++++++++++")

