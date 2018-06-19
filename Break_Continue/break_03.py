'''
Created on Aug 15, 2014

@author: rocky
script to demo the working of "break" statement.
'''
while True:
    reply=input("Enter the String : ")
    if reply=='stop':
        break
    elif not reply.isdigit():
        print("Bad! "*8)
    else:
        print(int(reply)**2)
print("End of Script")