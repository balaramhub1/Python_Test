'''
Created on Apr 15, 2015

@author: Administrator
'''

import sqlite3
con1=sqlite3.connect("C:\\Documents and Settings\\Administrator\\DbOne.db")
cur=con1.cursor()

cur.execute("select * from tbOne")
rowList=cur.fetchall()
print(rowList)
rowlen=len(rowList)
idList=[]
print("The length of data set is : ",rowlen)
for x in range(0,rowlen):
    idList.append(rowList[x][0])
print(idList)

id1=int(input("Enter the Employee ID : "))
for xid in idList:
    if id1==xid:
        idExist=True
        print("Id already exists...")
        break
    else:
        idExist=False

if not idExist:
    name1=input("Enter the Name : ")
    age1=int(input("Enter the Age : "))
    sal1=int(input("Enter the Salary : "))
    cur.execute("insert into tbOne (Id,eName,eAge,eSal) values (?,?,?,?)",(id1,name1,age1,sal1))
    con1.commit()

print("Record inserted successfully....")
