'''
Created on Sep 9, 2014

@author: rocky
creating a class
'''
class Employee:
    eCount=0
    def __init__(self,name,age,dept,salary,dob):
        self.name=name
        self.age=age
        self.dept=dept
        self.salary=salary
        self.dob=dob
        Employee.eCount +=1
    
    def countDisp(self):
        print("No of Employees are : ",Employee.eCount)
    
    def empDisp(self):
        print("Name of Employee is : ",self.name)
        print("Age of Employee is : ",self.age)
        print("Dept of Employee is : ",self.dept)
        print("Salary of Employee is : ",self.salary)
        print("Dob of Employee is : ",self.dob)
    
    def inputEmp(self):
        self.name=input("Enter the Name of Employee : ")
        self.age=int(input("Enter the Age of Employee : "))
        self.dept=input("Enter the Dept of Employee : ")
        self.salary=int(input("Enter the Salary of Employee : "))
        self.dob=input("Enter the D.O.B of Employee : ")

emp1=Employee('n',0,'dept',0,'dob')
emp1.inputEmp()
emp1.countDisp()
emp1.empDisp()
