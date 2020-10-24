'''
Created on Jul 23, 2014

@author: HOME
The script is to show the nesting of if else..blocks
'''
lname=['ajay','anil','anjali']
print("list of names is :",lname)
urname=input("Please Enter your name : ")
if (urname =='ajay' or urname == 'anil' or urname == 'anjali'):
    urname=urname.title()
    gender=input("Please enter your Gender (M or F ): ")
    if (gender=='M'or gender=='m'):
        print("Your name is {0}{1}".format('Mr.',urname))
    elif (gender=='F'or gender=='f'):
        print("Your name is {0}{1}".format('Mrs.',urname))
    else:
        print("Which gender are you!!!")
    print("Thank you...!!!")
else:
    print("You are a Stranger....")