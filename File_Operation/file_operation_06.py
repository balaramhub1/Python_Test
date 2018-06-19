'''
Created on Aug 19, 2014

@author: rocky
Script to demo writing into a file.
'''
fopen=open('test2.txt','w')
fopen.write("Hello this is the first line into the file test2.txt. \n")
print("Line 1 is writen into the file")
fopen.close()
