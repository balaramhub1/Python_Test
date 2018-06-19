'''
Created on Feb 9, 2015

@author: Administrator
Script to find the user name and domain of mail id's
'''
email_id='abcd@xyz.com'
#email_id=input("Enter the Email id : ")
elen=len(email_id)
print("Length of email id is : ",elen)
print("No of '@' in the string is :",email_id.count('@'))
for x in email_id:
    if x=='@':
        pos=email_id.index(x)
        print(x,"is found at : ",email_id.index(x)+1)
        
# use partition function to separate string
# and add individual output string into a tuple 
print("using partition function")
tu=email_id.partition('@')
print(email_id.partition('@'))
for y in tu:
    if y!='@':
        print(y)
# use split function, returns a string
print("Using split function")
print(email_id.split('@',maxsplit=1))