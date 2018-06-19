'''
Created on Jul 14, 2014

@author: HOME
'''
print("Basic arithmatic-1 operations in Python.")
a=2
b=5
c=2.345
d=0.3
e=4 +3j
f=-6
print("Value of a =" , a ,"\nValue of b =",b , "\nValue of c =",c,"\nValue of d =",d)
#this line is to print multiple lines with their values.
print("Value of e =",e)
print("Real part of e =",e.real) # display the real part of a complex number
print("Imaginary part of e =",e.imag) # display the imaginary part of complex number
print("Value of f =",f)
print("Integer 'a' ",a, " + Integer 'b' ",b," =",a+b)
print("Integer 'a' ",a, " + Float 'c' ",c," =",a+c)
print("Integer 'a' ",a, " * Float 'c' ",c," =",a*c)
print("Integer 'b' ",b, " / Float 'c' ",c," =",b/c)
print("Integer 'b' ",b, " / Float 'c' ",c," =",b//c)
#above // truncates the fraction part to display only the integer part of the result.
print("Integer 'b' ",b, " % Integer 'a' ",a," =",b%a)
#above % only displays the reminder of the division b/a.