'''
Created on Jul 17, 2014

@author: HOME
The script is to check for the function of string methods
1) s.islower(), 2) s.isupper(), 3) s.isnumeric(), 4. s.isprintable(), 5. s.isspace()
 
'''
var1='SUN'
var2='Moon'
var3='earth'
var4='23.45'
var5='43b'
var6=' '
var7=''
var8='\t' # or '\n','\a','\b'...
print("var1 '{0}' islower() : ".format(var1),var1.islower())
print("var1 '{0}' isupper() : ".format(var1),var1.isupper())
print("var1 '{0}' isnumeric() : ".format(var1),var1.isnumeric())
print("var1 '{0}' isprintable() : ".format(var1),var1.isprintable())
print("var1 '{0}' isspace() : ".format(var1),var1.isspace())
print("var1 '{0}' islower() : ".format(var2),var2.islower())
print("var1 '{0}' isupper() : ".format(var2),var2.isupper())
print("var1 '{0}' islower() : ".format(var3),var3.islower())
print("var1 '{0}' isupper() : ".format(var3),var3.isupper())
print("var1 '{0}' isspace() : ".format(var6),var6.isspace())
print("var1 '{0}' isspace() : ".format(var7),var7.isspace())
print("var1 '{0}' isprintable() : ".format(var8),var8.isprintable())
print("var1 '{0}' isnumeric() : ".format(var4),var4.isnumeric())
print("var1 '{0}' isnumeric() : ".format(var5),var5.isnumeric())
