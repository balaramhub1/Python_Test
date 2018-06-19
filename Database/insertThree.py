'''
Created on Apr 18, 2015

@author: Administrator
'''
import sqlite3
class member():
    mCount=0
    def __init__(self):
        self.Id=0
        self.Name=""
        self.Age=0
        self.Sal=0
        member.mCount+=1
    
    def inputMem(self):
        self.Id=int(input("Enter the Employee Id : "))
        m1.dbCheck()
               
    def dbCon(self):
        self.con=sqlite3.connect("C:\\Documents and Settings\\Administrator\\DbOne.db")
        self.cur1=self.con.cursor()
    
    def dbCheck(self):
        idList=[]
        self.cur1.execute("select * from tbTwo")
        self.rows=self.cur1.fetchall()
        rlen=len(self.rows)
        for x in range(0,rlen):
            idList.append(self.rows[x][0])
        print("List of ID's : ",idList)
        for xid in idList:
            if xid==self.Id:
                idExist=True
                print("ID already exists..please enter a unique ID...")
                break
            else:
                idExist=False
                    
        if not idExist:
            self.Name=input("Enter the Employee Name : ")
            self.Age=int(input("Enter the Employee Age : "))
            self.Sal=int(input("Enter the Employee Sal : "))
                     
        
    def dbIns(self):
        if self.Name!="":
            self.cur1.execute("insert into tbTwo (mId,mName,mAge,mSal)values(?,?,?,?)",(self.Id,self.Name,self.Age,self.Sal))
            self.con.commit()
            print("Data inserted successfully..")
                
    def dbDisp(self):
        self.cur1.execute("select * from tbTwo")
        self.rows=self.cur1.fetchall()
        print(self.rows)

if __name__=="__main__":
    m1=member()
    m1.dbCon()
    m1.inputMem()
    m1.dbIns()
    print("Existing data listed below:")
    print('-'*27)
    m1.dbDisp()
