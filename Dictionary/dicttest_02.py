'''
Created on May 10, 2014

@author: ROCKSTAR
'''
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for k in stock:
    print(k)
    print("Stock : ",stock[k])
    print("Price : ",prices[k])

