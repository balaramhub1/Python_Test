'''
Created on Jul 25, 2014

@author: HOME
A basic example of Function in Python.
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
add(a,b)
subs(a,b)
mult(a,b)
divs(a,b)
