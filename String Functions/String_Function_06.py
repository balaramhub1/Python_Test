'''
Created on Jul 16, 2014

@author: HOME
The script is to see the String methods 1) s.isalnum(), 2) s.isalpha(), 3) s.isdecimal(), 
4) s.isdigit(), 5) s.isidentifier()

'''
var1='abcd123'
var2='lkjlk'
var3='2334'
var4='9876.834'
var=['1dfdk','_sdf23','dsjdk','ddf kj']
print("is {0} alphanum : ".format(var1),var1.isalnum())
print("is {0} alphanum : ".format(var2),var2.isalnum())
print("is {0} alphanum : ".format(var3),var3.isalnum())
print("is {0} alphanum : ".format(var4),var4.isalnum())
print("is {0} decimal : ".format(var3),var3.isdecimal())
print("is {0} decimal : ".format(var4),var4.isdecimal())
print("is {0[0]} identifier : ".format(var),var[0].isidentifier())
print("is {0[1]} identifier : ".format(var),var[1].isidentifier())
print("is {0[2]} identifier : ".format(var),var[2].isidentifier())
print("is {0[3]} identifier : ".format(var),var[3].isidentifier())
print("is {0} digit : ".format(var3),var3.isdigit())

