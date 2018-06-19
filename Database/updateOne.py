'''
Created on Apr 17, 2015

@author: Administrator

Script to update data base table
'''
import sqlite3
con=sqlite3.connect("C:\\Documents and Settings\\Administrator\\DbOne.db")
cur=con.cursor()
cur.execute("select * from tbOne")
rows=cur.fetchall()
print(rows)
# update code
cur.execute("update tbOne set eName=?,eAge=?,eSal=? where Id=?",('chintu',33,121111,101))
print("Updated Data")
cur.execute("select * from tbOne")
rows=cur.fetchall()
print(rows)
con.commit()