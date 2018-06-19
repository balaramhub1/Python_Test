'''
Created on Jul 30, 2014

@author: rocky
basic function working in python.
'''
a=0
b=0
def add(x,y):
    c=x+y
    print("Summation of 1st and 2nd number is : ",c)

def subs(x,y):
    c=x-y
    print("Subtraction of 1st and 2nd number is : ",c)
    
def mult(x,y):
    c=x*y
    print("Multiplication of 1st and 2nd number is : ",c)
    
def divs(x,y):
    c=x/y
    print("Division of 1st and 2nd number is : ",c)
    
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

ans=input("Do you want to continue ..press(y/Y) : ")
while(ans=='y' or ans=='Y'):
    opt=int(input("Press your option 1/2/3/4..:"))
    if (opt==1):
        add(a,b)
    elif (opt==2):
        subs(a,b)
    elif (opt==3):
        mult(a,b)
    elif (opt==4):
        divs(a,b)
    else:
        print("you have selected a wrong option.")
    ans=input("Do you want to continue ..press(y/Y) : ")
print("End of Script")
    
        