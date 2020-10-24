'''
Created on Jun 14, 2020

String functions for fixed length operations, s.centre(), s.ljust()
@author: beherb2
'''

s="center"
print(s.center(20))

# using the fill char
print(s.center(20,"*"))


# using the fill character on right side and string as left justified
print(s.ljust(20,"_"))

# using the fill character on left side and string as right justified
print(s.rjust(20,"_"))