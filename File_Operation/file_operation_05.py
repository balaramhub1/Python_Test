'''
Created on Aug 17, 2014

@author: rocky
Script to read a file byte by byte
'''
fopen=open('test1.txt','r')
char=fopen.read(1)
while char:
    print(char,end="")
    # prints a character without a space or newline.
    char=fopen.read(1)
fopen.close()