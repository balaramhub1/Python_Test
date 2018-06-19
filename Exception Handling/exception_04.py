'''
Created on Aug 29, 2014

@author: rocky
Script to check exception when file doesnt exists.
'''
fopen=None
try:
    fopen=open('test3.txt','r') # the file does not exist.
    while True:
        print(fopen.readline())
        
except FileNotFoundError:
    print("File not found.")

finally:
    if fopen:
        fopen.close()
        print("Closed the File..")
