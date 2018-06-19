'''
Created on Jan 29, 2015

@author: rocky
Script to reverse a String
'''
st=input("Enter the String : ")
ts=[]
stlen=len(st)
stlen2=stlen
print("String length is :",stlen)
for i in range(stlen2-1,-1,-1):
    for j in range(1,stlen):
        ts.append(st[i])
        break
ts=''.join(ts)
print(ts)   
