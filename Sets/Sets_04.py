'''
Created on Jun 14, 2020

- pop()
- remove()
- discard()
- clear()
- del

@author: beherb2
'''
s={100,200,300,400,500,600}

# removes the first element
r=s.pop()
print(r)
print(s)

s.remove(400)
print(s)

s.discard(400)
print(s)

# it will remove the element if found, if not found will do nothing
s.discard(500)
print(s)

# clear all the elements of the set
s.clear()
print(s)





