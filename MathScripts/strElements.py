'''
Created on Jan 29, 2015

@author: rocky
Script to display the string elements
'''
st=input("Enter the String : ")
print("First to Sixth element in the String : ",st[0:7])
print("Second Element of'",st,"'is :",st[2])
print("Length of the String is : ",len(st))
ind=0
for s in st:
    print(ind,": element is :",s)
    ind=ind+1
