'''
Created on Jul 17, 2014

@author: HOME
'''
import String_01

str1="hello how are you"
num1=123.456
print("{0:25}".format(str1)) # minimum width of 25 .
print("{0:>25}".format(str1)) # right aligned by > operator.
print("{0:<25}".format(str1)) # left aligned by < operator.
print("{0:^25}".format(str1)) # center aligned by ^ operator.
print("{0:%^25}".format(str1)) # center aligned by ^ operator and fill with %.
print("{0:.12}".format(str1))
print("{0:.4}".format(num1))
print("{0:012}".format(num1)) # 0 padding for width =12
print("{0:0=12}".format(num1))
print("{0:0=12}".format(-num1))
