'''
Created on Aug 29, 2014

@author: rocky
Script to demo exception when file is empty.
'''
fopen=None
try:
    fopen=open('E:\eclipse-java-helios-SR1-win32\workspace\Python_Test\File_Operation\test4.txt','r')
    while fopen:
        x=fopen.readline()
        if (x=="" or x==" "):
            print("The file is blank...")
            break
        else:
            fopen.seek(0)
            print(fopen.read())
            break
except FileNotFoundError:
    print("file not found")
finally:  
    fopen.close() 
# E:\\eclipse-java-helios-SR1-win32\\workspace\\Python_Test\\File_Operation

