'''
Created on Apr 4, 2015

@author: Administrator
Script to demonstrate the database connectivity
database used is SQLite3
'''
import sqlite3
con1=sqlite3.connect("C:\\Documents and Settings\\Administrator\\DbOne.db")
cur=con1.cursor()
cur.execute('select * from tbOne')
row1=cur.fetchall()
rl=len(row1)
print("number of elements in result set is : ",rl)
for x in range(0,rl):
    print(row1[x][0])
