'''
Created on Jul 17, 2014

@author: HOME
The script is to see the function of T.index[x] and T.count(x) methods of Tuple
'''
list1=['hello','balaram']
color = ("red","green","blue",list1)
fruit =(5,"lemon",8,"berry",color,"grapes","cherry")
numtup=(4,6,3,2,5,23,3,2,4,2,3,5)
print("Elements of List1 are : ",list1)
print("Elements of tuple 'color' are : ",color)
print("Elements of tuple 'fruit' are : ",fruit)
print("Index value of 'hello' is : ",fruit[4][3][0].index('hello'))
print("Index value of 'blue' is : ",fruit[4].index('blue'))
print("count of '3' in numtup is : ",numtup.count(3))
print("Index of '3' in numtup is : ",numtup.index(3))

