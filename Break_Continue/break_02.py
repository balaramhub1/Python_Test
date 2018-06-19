'''
Created on Aug 6, 2014

@author: rocky
Script to show the working of "break" statement.
'''
while True:
    name=input("Enter the Name : ")
    if name=='stop':break
    age=int(input("Enter the Age : "))
    print(name," ",age)
print("End of script reached")
        