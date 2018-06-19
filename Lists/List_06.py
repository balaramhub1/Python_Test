'''
Created on Jul 19, 2014

@author: HOME
The script to show nested list and accessing its elements.
'''
lsta=[[1,2,3],
      [4,5,6],
      [7,8,9],
      ]
print(lsta)
x=0
y=0
for x in lsta:
    for y in lsta:
        print(lsta[x][y])
        x+=1
    y+=1
        

