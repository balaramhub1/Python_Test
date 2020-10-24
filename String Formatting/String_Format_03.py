'''
Created on Jan 23, 2020

@author: beherb2
'''
# demonstration of String formating using sep parameter

x=10
y=14
print("{0} + {1} = {2}".format(x,y,x+y))

print("hello","world",sep="hhhh")
print("hello","world",sep="---hhhh+++")
print("hello","world",sep="")
print("hello","world")


# String formating using %s,%d....
name="Abhinav"
age=23
print("Your Name is : %s"%name)
print("Hello !! %s, your age is %d"%(name,age))

print("Your marks are : %f"%77.6)

# To limit the displaye to 2 decimal point
print("Your marks are : %.2f"%77.6)

