'''
Created on Jul 24, 2014

@author: HOME
'''
def sum_n():
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
    

ans=input("Enter y/Y if you want to continue : ")
while(ans=='y' or ans=='Y'):
    sum_n()
    ans=input("Enter y/Y if you want to continue : ")
print("End of Script")

