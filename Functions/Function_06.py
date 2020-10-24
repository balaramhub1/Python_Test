'''
Created on Jun 14, 2020

Variable length keyword parameters/ arguments

@author: beherb2
'''
# ** is used for keyword arguments
# *args - will pass all arguments as a tuple
# **args - will pass all arguments as dictionary

def getDetails(**kwargs):
    print(kwargs)

getDetails(name="ABC",email="abc@gmail.com",contact=767676,dob="12-01-2020")

getDetails(name="ABC",email="abc@gmail.com",contact=767676)

getDetails(name="ABC",email="abc@gmail.com",dob="12-01-2020")

