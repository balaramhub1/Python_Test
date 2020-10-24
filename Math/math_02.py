'''
Created on Jun 14, 2020

Demonstrate some math functions from math module

@author: beherb2
'''
import math


l=[0.1]*10
print(l)

print(sum(l))

print(math.fsum(l))

num1=15.5559
# print the floor value of num1 i.e lower bound
print(math.floor(num1))

# print the ceiling value of num1, i.e upper bound
print(math.ceil(num1))


# find square root of a number
print(math.sqrt(24))

# find factorial of a number
print(math.factorial(4))

# mod of a number
print(math.modf(num1))

print(math.fmod(19, 5))

# power function
print(math.pow(5, 2))

# trignometric
print(math.sin(math.degrees(90)))

