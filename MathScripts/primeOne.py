'''
Created on Jan 28, 2015

@author: rocky
Script to check the number is Prime or Not
'''
num=int(input("Enter the Number : "))
for i in range(2,num):
    if(num%i==0):
        print("Composite")
        break
else:
    print(num,": is Prime")

