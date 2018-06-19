'''
Created on Aug 17, 2014

@author: rocky
Script to open a txt file and read
'''
afile=open('test1.txt','r')
print("using readline()")
print(afile.readline()) 
'readline() reads only one line from the file'

print("using readline(2)")
print(afile.readline(2))
'readline(2) reads only 2 characters from the line'

print("using read(11)")
print(afile.read(11))
'read(11) reads only 11 character of the line from previous control position.'

print("using read()")
print(afile.read())
'read() reads all the lines of the file from previous control position.'
