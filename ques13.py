#Develop a `Shape` class with a method `area()`. 
# Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        print("The areas can be calculated for any shape")
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"The area of square is:{self.side*self.side}")
class Triangle(Shape):
    def __init__(self,height,base):
        self.height=float(height)
        self.base=float(base)
        
    def area(self):
        tarea=(0.5)*self.height*self.base
        print(f"The area of triangle is:{tarea:.2f}")
s=Square(5)
s.area()
t=Triangle(7,5)
t.area()
