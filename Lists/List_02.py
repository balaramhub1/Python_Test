'''
Created on Jan 1, 2008

@author: HOME
The script is to show the sequence unpacking.
List assignments,slice assignments
'''
li_fruit=['mango','apple','orange','banana','cherry']
x,*y,z=li_fruit
print(x)
print(y)
print(z)
lia=[x*2 for x in 'abcd']
print(lia)
lia=li_fruit+lia[1:3]
print(lia)



