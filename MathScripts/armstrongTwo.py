'''
Created on Jan 28, 2015

@author: rocky
Script to display the armstrong numbers in a range.
'''
r=int(input("Enter the Range : "))
for i in range(1,r):
    temp=i
    total=0
    while(i>0):
        digit=i%10;
        total=total+digit**3
        i=i//10
    if(temp==total):
        print(temp,": is Amstrong Number")
    else:
        pass
        #print(temp,": is Not Amstrong Number")