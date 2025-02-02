class Person:
    def __init__(self,name):
        self.name=name
    def showP(self):
        print(f"The person name is:{self.name}")
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name) 
        self.emp_id=emp_id
    def showE(self):
        print(f"The emp id is:{self.emp_id}")
class Manager(Employee):
    def __init__(self,name,emp_id,dept):
        super().__init__(name,emp_id) 
        self.dept=dept
    def approve_leave(self,days):
        print(f"Manager approved {days} days of leave for {self.name}. ")
m=Manager("Srii","6609","Csm")
m.showE()
m.showP()
m.approve_leave(5)


        