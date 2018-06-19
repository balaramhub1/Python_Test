'''
Created on Jul 14, 2014

@author: HOME
'''
print("Basic arithmatic-2 operations in Python.")
a=2
b=5
c=5.345
d=0.3
e=4 +3j
f=-6
print("Value of a =" , a ,"\nValue of b =",b , "\nValue of c =",c,"\nValue of d =",d)
#this line is to print multiple lines with their values.
print("Value of e =",e)
print("Real part of e =",e.real) # display the real part of a complex number
print("Imaginary part of e =",e.imag) # display the imaginary part of complex number
print("Value of f =",f)
print("Integer 'a'",a," % float ",d," =",a%d)
print("Integer 'b'",b," raised to the power of 'a'",a,"= ",b**a)
#raises b to the power of a
print("Integer 'a'",a,"raised to the power of 'b'",b,"= ",a**b)
#raises a to the power of b
print("Integer 'a'",a,"raised to the power of 'b' using pow(a,b) function",b,"= ",pow(a,b))
print("Negative of value of 'f' =",-f)
print("division of 'b' by 'a' gives",divmod(b,a))
#Returns the quotient and reminder as a tuple
print("Rounding of 'b' by 'a' gives",round(c,a))
#Rounding of b to a decimal places.




