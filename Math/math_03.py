'''
Created on Jun 14, 2020

Usage of Random module

@author: beherb2
'''
import random

print(random.random())


# Choose a random number from a list
l=[1,2,3,4,5,6]
print(random.choice(l))

# generate a random number between a range
print(random.randint(10,100))

# end number is not included
print(random.randrange(10,100))

# generate a floating random number
print(random.uniform(10,20))

