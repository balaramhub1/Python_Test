'''
Created on Jun 6, 2020

Demonstrate continue statement

@author: beherb2
'''
l1=[10,20,30,40,50,60]
x=300
print("List is : ",l1)
print("Searching for : ",x)

for key,val in enumerate(l1):
    if val==x:
        print("Value matched at index : ",key)
        break
    else:
        continue
        print("Not Reachable code")
else: # optional else for 'for' loop.
    print("Value not matched")
    
print("After for loop")
    
       
   
        