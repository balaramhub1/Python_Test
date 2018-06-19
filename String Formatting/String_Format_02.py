'''
Created on Jul 17, 2014

@author: HOME
The script is to see the str.format() method for
1) sign character.
2) type characters.
3) comma seperated groups.
'''
x=123456
y=-456789
z=76758.45998 -2344.445j
print("Number 1 is [{0: }] and Number 2 is [{1: }]".format(x,y)) # space or - sign
print("Number 1 is [{0:+}] and Number 2 is [{1:+}]".format(x,y)) # force the sign character
print("Number 1 is [{0:-}] and Number 2 is [{1:-}] \n".format(x,y)) # -sign if needed.
print('#'*50,"\n")
print("{0:b} {0:o} {0:x} {0:X}".format(-y))
print("{0:#b} {0:#o} {0:#x} {0:#X}".format(-y))
print("{0:,}".format(x))# comma seperated group
print("{0.real:,.4f} {0.imag:,.4f}j".format(z))

