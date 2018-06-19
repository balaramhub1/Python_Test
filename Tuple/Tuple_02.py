'''
Created on Jul 17, 2014

@author: HOME
The script is to see the access to nested tuples.
'''
list1=['hello','balaram']
color = ("red","green","blue",list1)
fruit =(5,"lemon",8,"berry",color,"grapes","cherry")
print("Elements of tuple 'color' are : \n",color)
print("Elements of tuple 'fruit' are : \n",fruit)
print("Third element of tuple fruit is : ",fruit[2])
print("Fifth element of tuple fruit is : ",fruit[4])
print("Sixth element of tuple fruit is : ",fruit[5])
# print("Sixth element of tuple fruit is : ",fruit[5]) # error as fruit doesnt have a 6th element.  
print("'r' of grapes can be accessed by : ",fruit[5][1])
print(" 'balaram' can be accessed by : ",fruit[4][3][1])
print(" 'bal' can be accessed by : ",fruit[4][3][1][0:3])

