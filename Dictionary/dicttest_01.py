'''
Created on May 10, 2014

@author: ROCKSTAR
'''
prices={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock={"banana": 6, "apple": 0, "orange": 32, "pear": 15}

flist=["banana","apple","orange"]
#print prices.keys()
print(prices)
for k in prices.keys():
    print(k)
    print(prices[k])
    print(stock[k])
    
for j,l in prices.items():
    print(j,"'s price is : ",l)
    