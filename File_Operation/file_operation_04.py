'''
Created on Aug 17, 2014

@author: rocky
Script to read a file character by character
'''
fopen=open('test1.txt','r')
for s in fopen:
    print(s)
fopen.close()
'reading line with line numbers'
fopen=open('test1.txt','r')
for i in range(1,4):
    print(i," :",fopen.readline())
print(fopen.tell())
fopen.close()

    
