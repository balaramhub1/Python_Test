'''
Created on Sep 4, 2014

@author: rocky
Script to display current directory by using import.os
'''
import os
'''prints the current working directory'''
print(os.getcwd())
'''prints the constant string used by os to refer to current directory'''
print(os.curdir)
''' prints the list of files/directories in the current directory by referring to curdir i.e " . " '''
print(os.listdir(path='.'))
path=input("Please enter the directory path : ")
''' prints the list of files/directories in the user provided path '''
print(os.listdir(path))
os.chdir(path)
print(os.getcwd())
