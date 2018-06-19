'''
Created on Jul 15, 2014

@author: HOME
The script is to see functionality of 1) s.strip(char)
2) s.swapcase() , 3) s.zfill(w)

'''
str1=" how "
str2="sTrinG tEst"
print(str1.strip())
print(str1.strip(' '))
print(str1.strip(' h'))
print(str1.rstrip('w '))
print(str2.swapcase())
print(str2.zfill(14))
