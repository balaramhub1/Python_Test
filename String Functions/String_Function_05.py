'''
Created on Jul 16, 2014

@author: HOME
The script is to see the function of str.format() method
1. Formatting is done by single string or number.
2. Formatting is done by taking values from list fruits.
3. Formatting is done by taking values from dictionary.
'''
str1="hello {0}, how are you"
name="rocky"
age=23
print('*'*40)
print(str1.format("balaram"))
print("{0}'s age is {1} yrs. ".format(name,age))
print("he is {attribute1},but his knees are {attribute2}\n".format(attribute1='strong',attribute2='weak'))
print('*'*40)
#str.format() method used values from list
fruits=['apple','orange','mango','bananna','pears','cherry']
print("we have '{0[1]}' and '{0[2]}' in stock \n".format(fruits))
print('*'*40)
dict1={'animal':'elephant','weight':1200}
print("The weight of {0[animal]} is {0[weight]} kgs".format(dict1))
