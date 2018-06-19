'''
Created on Apr 18, 2015

@author: Administrator
'''
class Employee:
    empCount=0
    def __init__(self):
        self.a=0
        self.b=0
        Employee.empCount+=1
    
    def numOut(self):
        print("value of a is : ",self.a)
        print("value of b is : ",self.b)
    
    def numIn(self):
        self.a=int(input("Enter the value of a : "))
        self.b=int(input("Enter the value of b : "))
        
e1=Employee()
e1.numIn()
e1.numOut()
e2=Employee()
e2.numIn()
e2.numOut()

print("No of Employees is : ",Employee.empCount)