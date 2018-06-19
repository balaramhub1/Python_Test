'''
Created on May 14, 2014

@author: rocky
'''
prices={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock={"banana": 6, "apple": 0, "orange": 32, "pear": 15}
new_stock={}

flist=["banana","apple","orange"]
print(prices)
print(stock)
print(flist)

total=0
for k in flist:
    #for k in stock:
    if stock[k]>0:
        print(k)
        total+=prices[k]
        
print("Total Shopping done is : ",total)
            
        
        
    