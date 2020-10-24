'''
Created on Jun 14, 2020

Parameter passing techniques

- variable length parameters

@author: beherb2
'''
l=[100,200,300,400,500,600]
print(l)

l.append(700)
print(l)

def addValue(*args):
    print(args)
        
    for x in args:
        l.append(x)
    return l
    
result=addValue()
print(result)

result=addValue(4,5,6)
print(result)

result=addValue(887,88)
print(result)

