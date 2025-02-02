class Student :
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def get_details(self):
        print(f'The student name  is :{self.name}\n The roll num is:{self.rollnumber}')
student=Student("Srikrupa",6609)
print(student.get_details())