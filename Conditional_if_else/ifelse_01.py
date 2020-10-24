'''
Created on Jul 22, 2014

@author: HOME
'''
import random
n=random.randint(0,10)
print("Random number 'n' is : ",n)
num=int(input("plese enter a decimal number : "))
num=num+n
print(num)
if num<= 5:
    print("low random number generated")
elif (num>=5 and num<=10):
    print("mid random number generated")
else :
    print("high random number generated")


