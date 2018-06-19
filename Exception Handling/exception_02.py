'''
Created on Aug 16, 2014

@author: rocky
Script to demo exception handling 
'''
while True:
    try:
        x=int(input("Enter the First Number (x): "))
        y=int(input("Enter the Second Number (y): "))
        val=x/y
        print("x/y is : ",val)
    except:
        print("invalid input...please try again..")
    else:
        break