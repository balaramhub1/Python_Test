'''
Created on Jun 14, 2020

Default parameters in Functions

Ex: create a function to generate a password of 8 char length
1 - upper case char
1 - lower case char
1 - special char
5 - digits

@author: beherb2
'''
import random

# ASCII representations of English characters
print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))

# default parameter length=8
def generatePass(passLen=8):
    
    # list of special char
    l=["!","@","#","$","&","_"]
    
    # cast it to character
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digits=str(random.randint(10000,99999))
    password=upper+lower+special+digits
    
    # Take a sample from the password
    l1=random.sample(password,passLen)
    password="".join(l1)
    print(password)
    return password

passw= generatePass()
print(passw)

# Keyword parameters

def validateLogin(username,password):
    if username=="ABC" and password=="Abc@123":
        print("Valid Login")
    else:
        print("Invalid Login")


validateLogin("ABC","ABC@124")
validateLogin("ABC", "Abc@123")

# Function call with parameter with keyword
validateLogin(password="Abc@123", username="ABC")

s="Hello how are you"
l=["Hello","how","are","you"]
print(s)
print(s,sep=",",end="$")
print()

print("hello","how","are","you")
print("hello","how","are","you",sep=",",end="$")
