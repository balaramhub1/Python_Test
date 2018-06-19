'''
Created on Jul 23, 2014

@author: HOME
'''
x=0
total=0
y=input("Enter the Number : ")
print(y.isdigit())
y=int(y)
while(x<=y):
    total+=x
    print("Value of x is : ",x)
    print("Value of Sum is : ",total)
    x=x+1
print("Thank you..!!")
    
