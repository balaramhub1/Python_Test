
'''
Created on Jan 28, 2015

@author: rocky
Script to find prime numbers in a range
'''
r=int(input("Enter the Range : "))
li=[]
for x in range(1,r):
    for i in range(2,x):
        if(x%i==0):
            print(x,"Composite")
            break
    else:
        print(x,"Prime")    
        li.append(x) 
print(li)   