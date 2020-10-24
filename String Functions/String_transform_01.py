'''
Created on Jun 14, 2020

This script is to demonstrate String transformation i.e translation as per a mapping table
@author: beherb2
'''

s="Hello how are you, this is a great day for you!!"
s2="how"
t2="woh"
s3="you"
t3="uoy"

# create the mapping table
table1=str.maketrans(s2,t2)

# translate the String s, using the mapping table 'table1'

print(s.translate(table1))

table2=str.maketrans(s3,t3)

print(s.translate(table2))

