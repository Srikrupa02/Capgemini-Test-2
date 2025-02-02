class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def show(self):
        print(f"Employee name is:{self.name}\n Employee id is:{self.id}\n Employee dept is:{self.department}")
name=input("Enter name:")
id=int(input("Enter id:"))
department=input("Enter the dept:")
e=Employee(name,id,department)
e.show()
    
