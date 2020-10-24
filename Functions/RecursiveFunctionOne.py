'''
Created on Jun 14, 2020

Demonstrate Recursive function in python

@author: beherb2
'''

def getFactorial(num):
    if num==1:
        return 1
    else:
        return num*getFactorial(num-1)

result=getFactorial(5)
print(result)

# 5 * getFactorial(4)
#    4 * getFactorial(3)
#        3 * getFactorial(2)
#            2 * getFactorial(1)
#                1
            