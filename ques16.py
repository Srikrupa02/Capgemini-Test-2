from abc import ABC, abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass 
class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
rectangle = Rectangle(5, 3)
print(f"Rectangle area: {rectangle.calculate_area()}")  

circle = Circle(4)
print(f"Circle area: {circle.calculate_area():.2f}")  
