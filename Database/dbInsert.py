'''
Created on Apr 9, 2015

@author: Administrator
'''
import sqlite3
con1=sqlite3.connect("C:\\Documents and Settings\\Administrator\\DbOne.db")
cur=con1.cursor()

def dispData():
    cur.execute("select * from tbOne")
    rows=cur.fetchall()
    for r in rows:
        print(r)
def dbInsert():
    id1=int(input("Enter the Employee ID : "))
    name1=input("Enter the Name : ")
    age1=int(input("Enter the Age : "))
    sal1=int(input("Enter the Salary : "))
    
    cur.execute("insert into tbOne (Id,eName,eAge,eSal) values (?,?,?,?)",(id1,name1,age1,sal1))
    con1.commit()

dbInsert()
dispData()