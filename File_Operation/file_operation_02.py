'''
Created on Aug 17, 2014

@author: rocky
Script to demo the function of reading a file.
'''
afile=open('test1.txt','r')
print(afile.readline())
afile.close()
afile=open('test1.txt','r')
afile.seek(0)
print("Output of text file using readlines() method. ")
print(afile.readlines())

