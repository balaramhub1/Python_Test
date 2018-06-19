'''
Created on Jan 1, 2008

@author: HOME
The script is to see the basic functions of LIST.
'''
list1=[3,'hello',34,(4,'try'),'rock',8]
list2=['are',3,'&&']
list3=['star',345]
str1='aeroplane'
print(list1)
list4=list(str1)
print(list4)
print('-'.join(list4))
list5=list2+list3
print("list 5 =list3+list2 : ",list5)
print(list1[2])
print(list1[3])
print(list1[3][1])
print(list1[2:4])
print(list1[-3:-2])






