'''
Created on Aug 17, 2014

@author: rocky
Script to demo "seek()" function while file reading.
'''
fopen=open('test1.txt','r')
print(fopen.read())
fopen.seek(4)
'seek() takes the control to the specified position in the file.'
print(fopen.readline())
fopen.close()
print("Reading text file content using For Loop.")
fopen=open('test1.txt','r')
for x in fopen:
    print(x,end="")
fopen.close()
