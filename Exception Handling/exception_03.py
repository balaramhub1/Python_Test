'''
Created on Aug 16, 2014

@author: rocky
'''
while True:
    try:
        x=int(input("Enter the First Number (x): "))
        y=int(input("Enter the Second Number (y): "))
        val=x/y
        print("x/y is : ",val)
    except Exception:
        print("invalid input..",Exception)
        print("please try again..")
    else:
        break