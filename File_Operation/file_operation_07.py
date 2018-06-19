'''
Created on Aug 24, 2014

@author: rocky
Script to demo appending/writing into a file.
'''
fopen=open('test2.txt','a')
fopen.write("Hello this is the appended line into the file test2.txt. ")
print("Line is appended into the file")

fopen.close()
fopen=open('test2.txt','r')
print(fopen.read())
fopen.seek(0)
print(fopen.readlines())