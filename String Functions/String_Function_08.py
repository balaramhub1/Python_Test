'''
Created on Jun 14, 2020

Script to demonstrate index(), find() and rfind() methods on String

@author: beherb2
'''

s="HTML,CSS,PYTHON,DJANGO,PYTHON"

# check if python is present in the above string s
print("PYTHON" in s)

# print the index of "PYTHON"
print(s.index("PYTHON"))

# Find "PYTHON" in the string s
print(s.find("PYTHON"))

# Find substring from end, i.e right 
print(s.rfind("PYTHON"))
